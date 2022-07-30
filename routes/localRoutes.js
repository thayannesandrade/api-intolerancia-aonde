const router = require('express').Router()

const Local = require('../models/Local')


// Create - criação de dados
router.post('/', async (req, res) => {
    // req.body
    
    // {localidade: "Terreiro de Mãe Joana", ocorrido: "Pedrada nos filhos de santos", estado: "Rio de Janeiro"}
    const {localidade, ocorrido, estado} = req.body

    if(!localidade && !ocorrido && !estado) {
        res.status(422).json({error: 'Todos os campos são obrigatórios!'})
        return
    }

    const local = {
        localidade,
        ocorrido,
        estado
    }

    try {
        // criando dados
        await Local.create(local)

        res.status(201).json({message: 'Fato inserido com sucesso!'})

    } catch (error) {
        res.status(500).json({error: error})
    }
})

// Read - leitura de dados

router.get('/', async (req, res) => {

    try {
       const locals = await Local.find()
       res.status(200).json(locals)

    } catch (error) {
        res.status(500).json({error: error})
    }
})

router.get('/:id', async (req, res) => {
    // extrair dado da requisição pela url (req.params)
    const id = req.params.id

    try {
        const local = await Local.findOne({ _id: id })

        if(!local) {
            res.status(422).json({message: 'Fato não encontrado'})
        }

        res.status(200).json(local)

     } catch (error) {
         res.status(500).json({error: error})
     }
})

// Update - atualização dos dados (PUT, PATCH)
router.patch('/:id', async (req, res) => {
    const id = req.params.id

    const {localidade, ocorrido, estado} = req.body

    const Local = {
        localidade,
        ocorrido,
        estado
    }

    try {

    const updateLocal = await Local.updateOne({_id: id}, local)

    res.status(200).json(local)

    } catch (error) {
        res.status(500).json({ error: error })
    }
})

module.exports = router
