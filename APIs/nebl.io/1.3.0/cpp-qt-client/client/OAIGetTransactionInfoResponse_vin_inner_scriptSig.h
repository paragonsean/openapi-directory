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
 * OAIGetTransactionInfoResponse_vin_inner_scriptSig.h
 *
 * 
 */

#ifndef OAIGetTransactionInfoResponse_vin_inner_scriptSig_H
#define OAIGetTransactionInfoResponse_vin_inner_scriptSig_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetTransactionInfoResponse_vin_inner_scriptSig : public OAIObject {
public:
    OAIGetTransactionInfoResponse_vin_inner_scriptSig();
    OAIGetTransactionInfoResponse_vin_inner_scriptSig(QString json);
    ~OAIGetTransactionInfoResponse_vin_inner_scriptSig() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getRAsm() const;
    void setRAsm(const QString &r_asm);
    bool is_r_asm_Set() const;
    bool is_r_asm_Valid() const;

    QString getHex() const;
    void setHex(const QString &hex);
    bool is_hex_Set() const;
    bool is_hex_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_r_asm;
    bool m_r_asm_isSet;
    bool m_r_asm_isValid;

    QString m_hex;
    bool m_hex_isSet;
    bool m_hex_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetTransactionInfoResponse_vin_inner_scriptSig)

#endif // OAIGetTransactionInfoResponse_vin_inner_scriptSig_H
