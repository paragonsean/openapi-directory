/**
 * Neblio REST API Suite
 * APIs for Interacting with NTP1 Tokens & The Neblio Blockchain
 *
 * The version of the OpenAPI document: 1.3.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetTransactionInfoResponse_vin_inner_previousOutput.h
 *
 * 
 */

#ifndef OAIGetTransactionInfoResponse_vin_inner_previousOutput_H
#define OAIGetTransactionInfoResponse_vin_inner_previousOutput_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetTransactionInfoResponse_vin_inner_previousOutput : public OAIObject {
public:
    OAIGetTransactionInfoResponse_vin_inner_previousOutput();
    OAIGetTransactionInfoResponse_vin_inner_previousOutput(QString json);
    ~OAIGetTransactionInfoResponse_vin_inner_previousOutput() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getAddresses() const;
    void setAddresses(const QList<QString> &addresses);
    bool is_addresses_Set() const;
    bool is_addresses_Valid() const;

    QString getRAsm() const;
    void setRAsm(const QString &r_asm);
    bool is_r_asm_Set() const;
    bool is_r_asm_Valid() const;

    QString getHex() const;
    void setHex(const QString &hex);
    bool is_hex_Set() const;
    bool is_hex_Valid() const;

    double getReqSigs() const;
    void setReqSigs(const double &req_sigs);
    bool is_req_sigs_Set() const;
    bool is_req_sigs_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_addresses;
    bool m_addresses_isSet;
    bool m_addresses_isValid;

    QString m_r_asm;
    bool m_r_asm_isSet;
    bool m_r_asm_isValid;

    QString m_hex;
    bool m_hex_isSet;
    bool m_hex_isValid;

    double m_req_sigs;
    bool m_req_sigs_isSet;
    bool m_req_sigs_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetTransactionInfoResponse_vin_inner_previousOutput)

#endif // OAIGetTransactionInfoResponse_vin_inner_previousOutput_H
