// configurações iniciais
require('dotenv').config()
const express = require('express')
const mongoose = require('mongoose')
const app = express()

const port = process.env.PORT || 3000


// forma de ler json
app.use(
    express.urlencoded({
        extended: true
    })
)
app.use(express.json())


// rotas da api
const localRoutes = require('./routes/localRoutes')

app.use('/local', localRoutes)

// end point inicial
app.get('/', (req, res) => {
    // mostrar requisição
    res.json({ message: 'Oi, minha API funcionaaa'})
})


// delivery port
const DB_USER = process.env.DB_USER;
const DB_PASSWORD = encodeURIComponent(process.env.DB_PASSWORD)

mongoose
    .connect(
        `mongodb+srv://${DB_USER}:${DB_PASSWORD}@apicluster.5xuoktr.mongodb.net/?retryWrites=true&w=majority`
    )
    .then(() => {
        console.log('Conecatamos ao MongoDB')
        app.listen(port, () => {
            console.info("Aplicação rodando em:" + port)
        })

    })
    .catch((error) => console.log(error))
