# dashboard_project/visualization.py
import pandas as pd
import matplotlib.pyplot as plt
from google.cloud import bigquery
from logging_config import setup_logger
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator

logger = setup_logger()

# Custom styling
plt.style.use('seaborn')
COLOR_PALETTE = {
    'On Time': '#2ecc71',    # Green
    'Delayed': '#e74c3c',    # Red
    'Cancelled': '#f39c12'   # Orange
}

def generate_visualizations():
    """Generate and save flight status visualizations"""
    try:
        logger.info("Generating flight visualizations...")
        
        # 1. Load data from BigQuery
        df = _load_flight_data()
        
        # 2. Generate charts
        _create_status_bar_chart(df)
        _create_temporal_line_chart(df)
        
        logger.info("✅ Visualizations saved to dashboard/ directory")
    except Exception as e:
        logger.error(f"❌ Visualization error: {e}")
        raise

def _load_flight_data():
    """Load flight data from BigQuery"""
    client = bigquery.Client()
    query = """
        SELECT 
            PARSE_DATE('%Y-%m-%d', Departure_Date) AS date,
            Flight_Status AS status,
            COUNT(*) AS count
        FROM `your-project.airline_dataset.clean_delays`
        GROUP BY date, status
    """
    return client.query(query).to_dataframe()

def _create_status_bar_chart(df):
    """Create flight status distribution bar chart"""
    plt.figure(figsize=(10, 6))
    
    # Prepare data
    status_counts = df.groupby('status')['count'].sum().sort_values()
    
    # Create plot
    ax = status_counts.plot(
        kind='barh',
        color=[COLOR_PALETTE.get(x, '#3498db') for x in status_counts.index],
        edgecolor='black',
        width=0.8
    )
    
    # Customize appearance
    ax.set_title('Flight Status Distribution', pad=20, fontsize=14, fontweight='bold')
    ax.set_xlabel('Number of Flights', labelpad=10)
    ax.set_ylabel('')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    
    # Add value labels
    for i, v in enumerate(status_counts):
        ax.text(v + 20, i, f"{v:,}", color='black', ha='left', va='center')
    
    plt.tight_layout()
    plt.savefig('dashboard/status_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

def _create_temporal_line_chart(df):
    """Create flight status trends over time"""
    plt.figure(figsize=(12, 6))
    
    # Pivot data for plotting
    pivot_df = df.pivot(index='date', columns='status', values='count')
    
    # Create plot
    ax = pivot_df.plot(
        style='.-',
        markersize=8,
        color=[COLOR_PALETTE.get(x, '#3498db') for x in pivot_df.columns],
        linewidth=2,
        figsize=(12, 6)
    )
    
    # Customize appearance
    ax.set_title('Flight Status Trends Over Time', pad=20, fontsize=14, fontweight='bold')
    ax.set_xlabel('Date', labelpad=10)
    ax.set_ylabel('Number of Flights', labelpad=10)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('dashboard/status_trends.png', dpi=300, bbox_inches='tight')
    plt.close()
