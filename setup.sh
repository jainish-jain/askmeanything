mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
[theme]
primaryColor='#f63366'\n\
backgroundColor='#0e1117'\n\
secondaryBackgroundColor='#31333F'\n\
textColor='#fafafa'\n\
font='monospace'\n\
\n\
" > ~/.streamlit/config.toml