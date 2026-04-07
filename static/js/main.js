// Main JavaScript utilities
console.log('Product Placement Analysis Dashboard Loaded');

// Utility function to format numbers
function formatNumber(num) {
    return new Intl.NumberFormat('en-US').format(num);
}

// Utility function to format currency
function formatCurrency(num) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(num);
}

// Utility function to format percentage
function formatPercent(num) {
    return (num * 100).toFixed(2) + '%';
}

// Toast notification
function showNotification(message, type = 'info') {
    const alertClass = `alert-${type}`;
    const alert = document.createElement('div');
    alert.className = `alert ${alertClass} alert-dismissible fade show`;
    alert.role = 'alert';
    alert.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    const container = document.querySelector('main');
    if (container) {
        container.insertBefore(alert, container.firstChild);
        setTimeout(() => alert.remove(), 5000);
    }
}

// API helper
async function apiCall(endpoint, options = {}) {
    try {
        const response = await fetch(endpoint, options);
        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('API call failed:', error);
        showNotification('An error occurred. Please try again.', 'danger');
        throw error;
    }
}

// Chart configuration
const chartConfig = {
    responsive: true,
    hovermode: 'x unified',
    margin: {
        l: 60,
        r: 20,
        t: 40,
        b: 60
    }
};

// Color palette
const colorPalette = [
    '#0d6efd', // blue
    '#198754', // success
    '#ffc107', // warning
    '#0dcaf0', // info
    '#dc3545', // danger
    '#6f42c1', // purple
    '#e83e8c', // pink
    '#fd7e14'  // orange
];

// Debounce function
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Initialize tooltips (Bootstrap)
document.addEventListener('DOMContentLoaded', function() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});
