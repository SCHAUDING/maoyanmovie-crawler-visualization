// 票房榜前十点击事件
document.querySelector('a[href="#box-office"]').addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('chartFrame').style.display = 'block';
    document.getElementById('mapFrame').style.display = 'none';
    document.getElementById('yearlyFrame').style.display = 'none';
    document.getElementById('scatterFrame').style.display = 'none';
    document.getElementById('priceFrame').style.display = 'none';
    document.getElementById('typeCharts').style.display = 'none';
});

// 出品地区发布点击事件
document.querySelector('a[href="#region"]').addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('chartFrame').style.display = 'none';
    document.getElementById('mapFrame').style.display = 'block';
    document.getElementById('yearlyFrame').style.display = 'none';
    document.getElementById('scatterFrame').style.display = 'none';
    document.getElementById('priceFrame').style.display = 'none';
    document.getElementById('typeCharts').style.display = 'none';
});

// 各年票房数统计点击事件
document.querySelector('a[href="#yearly"]').addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('chartFrame').style.display = 'none';
    document.getElementById('mapFrame').style.display = 'none';
    document.getElementById('yearlyFrame').style.display = 'block';
    document.getElementById('scatterFrame').style.display = 'none';
    document.getElementById('priceFrame').style.display = 'none';
    document.getElementById('typeCharts').style.display = 'none';
});

// 票房与评分关系点击事件
document.querySelector('a[href="#rating"]').addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('chartFrame').style.display = 'none';
    document.getElementById('mapFrame').style.display = 'none';
    document.getElementById('yearlyFrame').style.display = 'none';
    document.getElementById('scatterFrame').style.display = 'block';
    document.getElementById('priceFrame').style.display = 'none';
    document.getElementById('typeCharts').style.display = 'none';
});

// 票价与观影人数关系点击事件
document.querySelector('a[href="#price"]').addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('chartFrame').style.display = 'none';
    document.getElementById('mapFrame').style.display = 'none';
    document.getElementById('yearlyFrame').style.display = 'none';
    document.getElementById('scatterFrame').style.display = 'none';
    document.getElementById('priceFrame').style.display = 'block';
    document.getElementById('typeCharts').style.display = 'none';
});

// 电影类型统计点击事件
document.querySelector('a[href="#genre"]').addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('chartFrame').style.display = 'none';
    document.getElementById('mapFrame').style.display = 'none';
    document.getElementById('yearlyFrame').style.display = 'none';
    document.getElementById('scatterFrame').style.display = 'none';
    document.getElementById('priceFrame').style.display = 'none';
    document.getElementById('typeCharts').style.display = 'flex';
});

document.addEventListener('DOMContentLoaded', function() {
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const iframe = entry.target;
                iframe.src = iframe.dataset.src;
                observer.unobserve(iframe);
            }
        });
    });

    document.querySelectorAll('iframe[data-src]').forEach(iframe => {
        observer.observe(iframe);
    });
}); 