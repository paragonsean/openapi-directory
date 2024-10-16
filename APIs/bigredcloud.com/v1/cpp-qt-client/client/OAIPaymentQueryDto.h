/**
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPaymentQueryDto.h
 *
 * 
 */

#ifndef OAIPaymentQueryDto_H
#define OAIPaymentQueryDto_H

#include <QJsonObject>

#include "OAIAcEntryDto.h"
#include "OAIAcudfValueDto.h"
#include <QByteArray>
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAcEntryDto;
class OAIAcudfValueDto;

class OAIPaymentQueryDto : public OAIObject {
public:
    OAIPaymentQueryDto();
    OAIPaymentQueryDto(QString json);
    ~OAIPaymentQueryDto() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAcCode() const;
    void setAcCode(const QString &ac_code);
    bool is_ac_code_Set() const;
    bool is_ac_code_Valid() const;

    QList<OAIAcEntryDto> getAcEntries() const;
    void setAcEntries(const QList<OAIAcEntryDto> &ac_entries);
    bool is_ac_entries_Set() const;
    bool is_ac_entries_Valid() const;

    QString getBankAccountCode() const;
    void setBankAccountCode(const QString &bank_account_code);
    bool is_bank_account_code_Set() const;
    bool is_bank_account_code_Valid() const;

    qint64 getBankAccountId() const;
    void setBankAccountId(const qint64 &bank_account_id);
    bool is_bank_account_id_Set() const;
    bool is_bank_account_id_Valid() const;

    qint64 getBookTranTypeId() const;
    void setBookTranTypeId(const qint64 &book_tran_type_id);
    bool is_book_tran_type_id_Set() const;
    bool is_book_tran_type_id_Valid() const;

    QList<OAIAcudfValueDto> getCustomFields() const;
    void setCustomFields(const QList<OAIAcudfValueDto> &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    QList<QString> getDetailCollection() const;
    void setDetailCollection(const QList<QString> &detail_collection);
    bool is_detail_collection_Set() const;
    bool is_detail_collection_Valid() const;

    double getDiscount() const;
    void setDiscount(const double &discount);
    bool is_discount_Set() const;
    bool is_discount_Valid() const;

    QDateTime getEntryDate() const;
    void setEntryDate(const QDateTime &entry_date);
    bool is_entry_date_Set() const;
    bool is_entry_date_Valid() const;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getNote() const;
    void setNote(const QString &note);
    bool is_note_Set() const;
    bool is_note_Valid() const;

    QString getPlaidTransactionId() const;
    void setPlaidTransactionId(const QString &plaid_transaction_id);
    bool is_plaid_transaction_id_Set() const;
    bool is_plaid_transaction_id_Valid() const;

    QDateTime getProcDate() const;
    void setProcDate(const QDateTime &proc_date);
    bool is_proc_date_Set() const;
    bool is_proc_date_Valid() const;

    QString getReference() const;
    void setReference(const QString &reference);
    bool is_reference_Set() const;
    bool is_reference_Valid() const;

    qint64 getSupplierId() const;
    void setSupplierId(const qint64 &supplier_id);
    bool is_supplier_id_Set() const;
    bool is_supplier_id_Valid() const;

    QByteArray getTimestamp() const;
    void setTimestamp(const QByteArray &timestamp);
    bool is_timestamp_Set() const;
    bool is_timestamp_Valid() const;

    double getTotal() const;
    void setTotal(const double &total);
    bool is_total_Set() const;
    bool is_total_Valid() const;

    QString getTransferBankCode() const;
    void setTransferBankCode(const QString &transfer_bank_code);
    bool is_transfer_bank_code_Set() const;
    bool is_transfer_bank_code_Valid() const;

    qint64 getTransferBankId() const;
    void setTransferBankId(const qint64 &transfer_bank_id);
    bool is_transfer_bank_id_Set() const;
    bool is_transfer_bank_id_Valid() const;

    double getUnallocated() const;
    void setUnallocated(const double &unallocated);
    bool is_unallocated_Set() const;
    bool is_unallocated_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_ac_code;
    bool m_ac_code_isSet;
    bool m_ac_code_isValid;

    QList<OAIAcEntryDto> m_ac_entries;
    bool m_ac_entries_isSet;
    bool m_ac_entries_isValid;

    QString m_bank_account_code;
    bool m_bank_account_code_isSet;
    bool m_bank_account_code_isValid;

    qint64 m_bank_account_id;
    bool m_bank_account_id_isSet;
    bool m_bank_account_id_isValid;

    qint64 m_book_tran_type_id;
    bool m_book_tran_type_id_isSet;
    bool m_book_tran_type_id_isValid;

    QList<OAIAcudfValueDto> m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    QList<QString> m_detail_collection;
    bool m_detail_collection_isSet;
    bool m_detail_collection_isValid;

    double m_discount;
    bool m_discount_isSet;
    bool m_discount_isValid;

    QDateTime m_entry_date;
    bool m_entry_date_isSet;
    bool m_entry_date_isValid;

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_note;
    bool m_note_isSet;
    bool m_note_isValid;

    QString m_plaid_transaction_id;
    bool m_plaid_transaction_id_isSet;
    bool m_plaid_transaction_id_isValid;

    QDateTime m_proc_date;
    bool m_proc_date_isSet;
    bool m_proc_date_isValid;

    QString m_reference;
    bool m_reference_isSet;
    bool m_reference_isValid;

    qint64 m_supplier_id;
    bool m_supplier_id_isSet;
    bool m_supplier_id_isValid;

    QByteArray m_timestamp;
    bool m_timestamp_isSet;
    bool m_timestamp_isValid;

    double m_total;
    bool m_total_isSet;
    bool m_total_isValid;

    QString m_transfer_bank_code;
    bool m_transfer_bank_code_isSet;
    bool m_transfer_bank_code_isValid;

    qint64 m_transfer_bank_id;
    bool m_transfer_bank_id_isSet;
    bool m_transfer_bank_id_isValid;

    double m_unallocated;
    bool m_unallocated_isSet;
    bool m_unallocated_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPaymentQueryDto)

#endif // OAIPaymentQueryDto_H
