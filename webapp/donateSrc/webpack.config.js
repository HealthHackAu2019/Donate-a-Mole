var path = require('path');
var HtmlWebpackPlugin =  require('html-webpack-plugin');

module.exports = {
    entry : './app/index.js',
    output : {
        path : path.resolve(__dirname , '../app/static/donate'),
        filename: 'donate_bundle.js'
    },
    module : {
        rules : [
            {test : /\.(js|jsx)$/, use:'babel-loader'},
            {test : /\.css$/, use:['style-loader', 'css-loader']},
            {test: /\.(png|jpg|gif)$/, use: ['file-loader']},
            {test: /\.svg$/, use: ['@svgr/webpack']}
        ]
    },
    mode:'development',
    plugins : []
}
