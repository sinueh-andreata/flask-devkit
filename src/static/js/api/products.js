import { showToast } from '../utils/toast.js';
import { showError } from '../utils/errors.js';
import { postData } from '../utils/fetchUtils.js';

export async function criarProduto(produto, csrfToken) {
    try {
        const data = await postData('/products/cadastrar', produto, {
            'X-CSRFToken': csrfToken
        });
        showToast('Produto criado com sucesso!', 'success');
        return data;
    } catch (error) {
        showError(error);
        throw error;
    }
}