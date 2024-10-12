/**
 * Cnab Online
 * Processe arquivos de retorno CNAB
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The OccurrenceAttributes model module.
 * @module model/OccurrenceAttributes
 * @version 1.0.0
 */
class OccurrenceAttributes {
    /**
     * Constructs a new <code>OccurrenceAttributes</code>.
     * @alias module:model/OccurrenceAttributes
     */
    constructor() { 
        
        OccurrenceAttributes.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OccurrenceAttributes</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OccurrenceAttributes} obj Optional instance to populate.
     * @return {module:model/OccurrenceAttributes} The populated <code>OccurrenceAttributes</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OccurrenceAttributes();

            if (data.hasOwnProperty('agency')) {
                obj['agency'] = ApiClient.convertToType(data['agency'], 'String');
            }
            if (data.hasOwnProperty('bank_tax')) {
                obj['bank_tax'] = ApiClient.convertToType(data['bank_tax'], 'Number');
            }
            if (data.hasOwnProperty('charged_agency')) {
                obj['charged_agency'] = ApiClient.convertToType(data['charged_agency'], 'String');
            }
            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
            }
            if (data.hasOwnProperty('code_name')) {
                obj['code_name'] = ApiClient.convertToType(data['code_name'], 'String');
            }
            if (data.hasOwnProperty('credit_date')) {
                obj['credit_date'] = ApiClient.convertToType(data['credit_date'], 'String');
            }
            if (data.hasOwnProperty('discount_value')) {
                obj['discount_value'] = ApiClient.convertToType(data['discount_value'], 'Number');
            }
            if (data.hasOwnProperty('document_number')) {
                obj['document_number'] = ApiClient.convertToType(data['document_number'], 'String');
            }
            if (data.hasOwnProperty('due_date')) {
                obj['due_date'] = ApiClient.convertToType(data['due_date'], 'String');
            }
            if (data.hasOwnProperty('iof_tax')) {
                obj['iof_tax'] = ApiClient.convertToType(data['iof_tax'], 'Number');
            }
            if (data.hasOwnProperty('is_dda')) {
                obj['is_dda'] = ApiClient.convertToType(data['is_dda'], 'String');
            }
            if (data.hasOwnProperty('is_payment')) {
                obj['is_payment'] = ApiClient.convertToType(data['is_payment'], 'Boolean');
            }
            if (data.hasOwnProperty('is_rejected_payment')) {
                obj['is_rejected_payment'] = ApiClient.convertToType(data['is_rejected_payment'], 'Boolean');
            }
            if (data.hasOwnProperty('liquidation_code')) {
                obj['liquidation_code'] = ApiClient.convertToType(data['liquidation_code'], 'String');
            }
            if (data.hasOwnProperty('liquidation_description')) {
                obj['liquidation_description'] = ApiClient.convertToType(data['liquidation_description'], 'String');
            }
            if (data.hasOwnProperty('mulct_value')) {
                obj['mulct_value'] = ApiClient.convertToType(data['mulct_value'], 'String');
            }
            if (data.hasOwnProperty('occurrence_date')) {
                obj['occurrence_date'] = ApiClient.convertToType(data['occurrence_date'], 'String');
            }
            if (data.hasOwnProperty('others_credits_value')) {
                obj['others_credits_value'] = ApiClient.convertToType(data['others_credits_value'], 'Number');
            }
            if (data.hasOwnProperty('our_number')) {
                obj['our_number'] = ApiClient.convertToType(data['our_number'], 'String');
            }
            if (data.hasOwnProperty('payer_allegation')) {
                obj['payer_allegation'] = ApiClient.convertToType(data['payer_allegation'], 'String');
            }
            if (data.hasOwnProperty('rebate_value')) {
                obj['rebate_value'] = ApiClient.convertToType(data['rebate_value'], 'Number');
            }
            if (data.hasOwnProperty('received_value')) {
                obj['received_value'] = ApiClient.convertToType(data['received_value'], 'Number');
            }
            if (data.hasOwnProperty('sequencial_number')) {
                obj['sequencial_number'] = ApiClient.convertToType(data['sequencial_number'], 'Number');
            }
            if (data.hasOwnProperty('title_value')) {
                obj['title_value'] = ApiClient.convertToType(data['title_value'], 'Number');
            }
            if (data.hasOwnProperty('wallet')) {
                obj['wallet'] = ApiClient.convertToType(data['wallet'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OccurrenceAttributes</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OccurrenceAttributes</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['agency'] && !(typeof data['agency'] === 'string' || data['agency'] instanceof String)) {
            throw new Error("Expected the field `agency` to be a primitive type in the JSON string but got " + data['agency']);
        }
        // ensure the json data is a string
        if (data['charged_agency'] && !(typeof data['charged_agency'] === 'string' || data['charged_agency'] instanceof String)) {
            throw new Error("Expected the field `charged_agency` to be a primitive type in the JSON string but got " + data['charged_agency']);
        }
        // ensure the json data is a string
        if (data['code'] && !(typeof data['code'] === 'string' || data['code'] instanceof String)) {
            throw new Error("Expected the field `code` to be a primitive type in the JSON string but got " + data['code']);
        }
        // ensure the json data is a string
        if (data['code_name'] && !(typeof data['code_name'] === 'string' || data['code_name'] instanceof String)) {
            throw new Error("Expected the field `code_name` to be a primitive type in the JSON string but got " + data['code_name']);
        }
        // ensure the json data is a string
        if (data['credit_date'] && !(typeof data['credit_date'] === 'string' || data['credit_date'] instanceof String)) {
            throw new Error("Expected the field `credit_date` to be a primitive type in the JSON string but got " + data['credit_date']);
        }
        // ensure the json data is a string
        if (data['document_number'] && !(typeof data['document_number'] === 'string' || data['document_number'] instanceof String)) {
            throw new Error("Expected the field `document_number` to be a primitive type in the JSON string but got " + data['document_number']);
        }
        // ensure the json data is a string
        if (data['due_date'] && !(typeof data['due_date'] === 'string' || data['due_date'] instanceof String)) {
            throw new Error("Expected the field `due_date` to be a primitive type in the JSON string but got " + data['due_date']);
        }
        // ensure the json data is a string
        if (data['is_dda'] && !(typeof data['is_dda'] === 'string' || data['is_dda'] instanceof String)) {
            throw new Error("Expected the field `is_dda` to be a primitive type in the JSON string but got " + data['is_dda']);
        }
        // ensure the json data is a string
        if (data['liquidation_code'] && !(typeof data['liquidation_code'] === 'string' || data['liquidation_code'] instanceof String)) {
            throw new Error("Expected the field `liquidation_code` to be a primitive type in the JSON string but got " + data['liquidation_code']);
        }
        // ensure the json data is a string
        if (data['liquidation_description'] && !(typeof data['liquidation_description'] === 'string' || data['liquidation_description'] instanceof String)) {
            throw new Error("Expected the field `liquidation_description` to be a primitive type in the JSON string but got " + data['liquidation_description']);
        }
        // ensure the json data is a string
        if (data['mulct_value'] && !(typeof data['mulct_value'] === 'string' || data['mulct_value'] instanceof String)) {
            throw new Error("Expected the field `mulct_value` to be a primitive type in the JSON string but got " + data['mulct_value']);
        }
        // ensure the json data is a string
        if (data['occurrence_date'] && !(typeof data['occurrence_date'] === 'string' || data['occurrence_date'] instanceof String)) {
            throw new Error("Expected the field `occurrence_date` to be a primitive type in the JSON string but got " + data['occurrence_date']);
        }
        // ensure the json data is a string
        if (data['our_number'] && !(typeof data['our_number'] === 'string' || data['our_number'] instanceof String)) {
            throw new Error("Expected the field `our_number` to be a primitive type in the JSON string but got " + data['our_number']);
        }
        // ensure the json data is a string
        if (data['payer_allegation'] && !(typeof data['payer_allegation'] === 'string' || data['payer_allegation'] instanceof String)) {
            throw new Error("Expected the field `payer_allegation` to be a primitive type in the JSON string but got " + data['payer_allegation']);
        }
        // ensure the json data is a string
        if (data['wallet'] && !(typeof data['wallet'] === 'string' || data['wallet'] instanceof String)) {
            throw new Error("Expected the field `wallet` to be a primitive type in the JSON string but got " + data['wallet']);
        }

        return true;
    }


}



/**
 * Retorna o número da agencia
 * @member {String} agency
 */
OccurrenceAttributes.prototype['agency'] = undefined;

/**
 * Tarifa bancária
 * @member {Number} bank_tax
 */
OccurrenceAttributes.prototype['bank_tax'] = undefined;

/**
 * Retorna a agencia cobradora (com o digito)
 * @member {String} charged_agency
 */
OccurrenceAttributes.prototype['charged_agency'] = undefined;

/**
 * Código de Ocorrência conforme o padrão CNAB
 * @member {String} code
 */
OccurrenceAttributes.prototype['code'] = undefined;

/**
 * Nome do código
 * @member {String} code_name
 */
OccurrenceAttributes.prototype['code_name'] = undefined;

/**
 * Retorna a data em que o dinheiro caiu na conta
 * @member {String} credit_date
 */
OccurrenceAttributes.prototype['credit_date'] = undefined;

/**
 * Valor de desconto
 * @member {Number} discount_value
 */
OccurrenceAttributes.prototype['discount_value'] = undefined;

/**
 * Retorna o número do documento do boleto
 * @member {String} document_number
 */
OccurrenceAttributes.prototype['document_number'] = undefined;

/**
 * Retorna a data de vencimento de boleto
 * @member {String} due_date
 */
OccurrenceAttributes.prototype['due_date'] = undefined;

/**
 * Retorna o valor do Imposto sobre operações financeiras (IOF)
 * @member {Number} iof_tax
 */
OccurrenceAttributes.prototype['iof_tax'] = undefined;

/**
 * Retorna de o boleto foi pago através do Débito Direto Autorizado
 * @member {String} is_dda
 */
OccurrenceAttributes.prototype['is_dda'] = undefined;

/**
 * Retorna se é para dar baixa no boleto
 * @member {Boolean} is_payment
 */
OccurrenceAttributes.prototype['is_payment'] = undefined;

/**
 * Retorno se é uma baixa rejeitada (Ex: pedido de baixa foi rejeitado)
 * @member {Boolean} is_rejected_payment
 */
OccurrenceAttributes.prototype['is_rejected_payment'] = undefined;

/**
 * Retorna o código de liquidação, normalmente usado para saber onde o cliente efetuou o pagamento
 * @member {String} liquidation_code
 */
OccurrenceAttributes.prototype['liquidation_code'] = undefined;

/**
 * Retorna a descrição do código de liquidação
 * @member {String} liquidation_description
 */
OccurrenceAttributes.prototype['liquidation_description'] = undefined;

/**
 * Retorna o valor de juros e mora
 * @member {String} mulct_value
 */
OccurrenceAttributes.prototype['mulct_value'] = undefined;

/**
 * Retorna a data da ocorrencia, o dia do pagamento
 * @member {String} occurrence_date
 */
OccurrenceAttributes.prototype['occurrence_date'] = undefined;

/**
 * Retorna o valor de outros creditos
 * @member {Number} others_credits_value
 */
OccurrenceAttributes.prototype['others_credits_value'] = undefined;

/**
 * Retorna o nosso número do boleto (sem o digito)
 * @member {String} our_number
 */
OccurrenceAttributes.prototype['our_number'] = undefined;

/**
 * Retorna a alegação do pagador (para erros)
 * @member {String} payer_allegation
 */
OccurrenceAttributes.prototype['payer_allegation'] = undefined;

/**
 * Retornna o valor dos abatimentos concedidos (depois da emissão)
 * @member {Number} rebate_value
 */
OccurrenceAttributes.prototype['rebate_value'] = undefined;

/**
 * Valor recebido
 * @member {Number} received_value
 */
OccurrenceAttributes.prototype['received_value'] = undefined;

/**
 * Retorna o numero sequencial da ocorrência no arquivo
 * @member {Number} sequencial_number
 */
OccurrenceAttributes.prototype['sequencial_number'] = undefined;

/**
 * Valor do título (valor do boleto)
 * @member {Number} title_value
 */
OccurrenceAttributes.prototype['title_value'] = undefined;

/**
 * Retorna o número da carteira do boleto
 * @member {String} wallet
 */
OccurrenceAttributes.prototype['wallet'] = undefined;






export default OccurrenceAttributes;

