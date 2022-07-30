const mongoose = require('mongoose')

const Local = mongoose.model('Local', {
    localidade: String,
    ocorrido: String,
    estado: String,
})

module.exports = Local