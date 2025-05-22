/**
 * Initialize charts for statistics page
 * This script handles the creation of all charts on the statistics page
 */
function initializeCharts(maleAvg, femaleAvg, ageData, durationData) {
    // Set up basic chart colors
    const colors = {
        primary: '#FF5C58',
        secondary: '#FF9F68',
        tertiary: '#A2D2FF',
        quaternary: '#CDB4DB',
        light: '#F4F4F4'
    };
    
    // Global Chart.js configurations
    Chart.defaults.font.family = "'Poppins', sans-serif";
    // Check for dark mode and set color accordingly
    const isDark = document.body.getAttribute('data-theme') !== 'light';
    Chart.defaults.color = isDark ? colors.light : '#333';
    Chart.defaults.borderColor = isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)';
    
    // Function to handle color change based on theme
    function getTextColor() {
        return isDark ? colors.light : '#333';
    }
    
    // Create gender comparison chart
    const genderChart = document.getElementById('genderChart');
    if (genderChart) {
        const ctx = genderChart.getContext('2d');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Men', 'Women'],
                datasets: [{
                    data: [maleAvg, femaleAvg],
                    backgroundColor: [
                        'rgba(162, 210, 255, 0.7)',
                        'rgba(255, 92, 88, 0.7)'
                    ],
                    borderColor: ['#A2D2FF', '#FF5C58'],
                    borderWidth: 2,
                    hoverOffset: 15
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { font: { size: 14 }, color: getTextColor() }
                    },
                    title: {
                        display: true,
                        text: 'Average calories by gender',
                        color: getTextColor(),
                        font: { size: 16, weight: 'bold' }
                    }
                },
                cutout: '60%',
                animation: { animateScale: true }
            }
        });
    }
    
    // Create age group chart
    const ageChart = document.getElementById('ageChart');
    if (ageChart && ageData && ageData.length > 0) {
        // Extract labels and values from data
        const ageLabels = ageData.map(item => item.group);
        const ageValues = ageData.map(item => item.value);
        
        // Create the chart
        const ageCtx = ageChart.getContext('2d');
        new Chart(ageCtx, {
            type: 'bar',
            data: {
                labels: ageLabels,
                datasets: [{
                    label: 'Average calories',
                    data: ageValues,
                    backgroundColor: [
                        'rgba(255, 159, 104, 0.7)',
                        'rgba(255, 92, 88, 0.7)',
                        'rgba(205, 180, 219, 0.7)',
                        'rgba(162, 210, 255, 0.7)'
                    ],
                    borderColor: [
                        '#FF9F68', '#FF5C58', '#CDB4DB', '#A2D2FF'
                    ],
                    borderWidth: 2,
                    borderRadius: 8,
                    maxBarThickness: 40
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: { color: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)' },
                        ticks: { color: getTextColor(), font: { weight: 'bold' } }
                    },
                    x: {
                        grid: { display: false },
                        ticks: { color: getTextColor(), font: { weight: 'bold' } }
                    }
                },
                plugins: {
                    legend: { display: false },
                    title: {
                        display: true,
                        text: 'Calories by age',
                        color: getTextColor(),
                        font: { size: 16, weight: 'bold' }
                    }
                }
            }
        });
    }
    
    // Create duration chart
    const durationChart = document.getElementById('durationChart');
    if (durationChart && durationData && durationData.length > 0) {
        // Extract labels and values from data
        const durationLabels = durationData.map(item => item.group);
        const durationValues = durationData.map(item => item.value);
        
        // Create the chart
        const durationCtx = durationChart.getContext('2d');
        new Chart(durationCtx, {
            type: 'line',
            data: {
                labels: durationLabels,
                datasets: [{
                    label: 'Average calories',
                    data: durationValues,
                    backgroundColor: 'rgba(205, 180, 219, 0.5)',
                    borderColor: '#CDB4DB',
                    borderWidth: 3,
                    tension: 0.4,
                    fill: true,
                    pointBackgroundColor: '#CDB4DB',
                    pointBorderColor: isDark ? colors.light : '#333',
                    pointRadius: 6,
                    pointHoverRadius: 8
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: { color: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)' },
                        ticks: { color: getTextColor(), font: { weight: 'bold' } }
                    },
                    x: {
                        grid: { display: false },
                        ticks: { color: getTextColor(), font: { weight: 'bold' } }
                    }
                },
                plugins: {
                    legend: { display: false },
                    title: {
                        display: true,
                        text: 'Calories by duration',
                        color: getTextColor(),
                        font: { size: 16, weight: 'bold' }
                    }
                }
            }
        });
    }
}

// Listen for theme changes and update charts
document.addEventListener('themeChanged', function(e) {
    // Reinitialize charts when the theme changes
    if (typeof MALE_AVG !== 'undefined' && typeof FEMALE_AVG !== 'undefined' 
        && typeof AGE_DATA !== 'undefined' && typeof DURATION_DATA !== 'undefined') {
        initializeCharts(MALE_AVG, FEMALE_AVG, AGE_DATA, DURATION_DATA);
    }
}); 