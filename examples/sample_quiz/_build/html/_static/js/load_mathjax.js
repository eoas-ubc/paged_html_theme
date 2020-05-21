(function () {
    // Retrieve previous config object if defined
    window.PagedConfig = window.PagedConfig || {};
    let beforePaged = window.PagedConfig.before;
    window.PagedConfig.before = async () => {
        if (beforePaged) await beforePaged();
        return new Promise((resolve, reject) => {
            var script = document.createElement("script");
            script.type = "text/javascript";
            var src = `https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js` + "?config=TeX-MML-AM_CHTML";
            if (location.protocol !== "file:" && /^https?:/.test(src))
                src = src.replace(/^https?:/, '');
            script.src = src;
            window.MathJax = {
                tex2jax: {
                    inlineMath: [['\\(','\\)']],
                    displayMath: [['\\[','\\]']],
                    displayAlign: "left",
                    processEscapes: true,
                    processEnvironments: true,
                    skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
                    TeX: { equationNumbers: { autoNumber: "AMS" },
                            extensions: ["AMSmath.js", "AMSsymbols.js", "color.js"] }
                },
                AuthorInit: () => {
                    MathJax.Hub.Register.StartupHook("Begin", () => {
                        MathJax.Hub.Queue(resolve);
                    });
                }
            };
            document.getElementsByTagName("head")[0].appendChild(script);
        });
    };
})();