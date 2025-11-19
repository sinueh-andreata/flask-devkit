import { criarProduto } from '../api/products.js';

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('formProduto');
    const csrfToken = document.getElementById('csrf_token').value;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        try {
            const novoProduto = await criarProduto(data, csrfToken); // Passe o token aqui
            console.log('Produto criado:', novoProduto);
        } catch (error) {
            console.error('Erro ao criar produto:', error);
        }
    });
});