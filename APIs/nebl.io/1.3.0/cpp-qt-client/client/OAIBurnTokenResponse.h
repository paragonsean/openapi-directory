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
 * OAIBurnTokenResponse.h
 *
 * 
 */

#ifndef OAIBurnTokenResponse_H
#define OAIBurnTokenResponse_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBurnTokenResponse : public OAIObject {
public:
    OAIBurnTokenResponse();
    OAIBurnTokenResponse(QString json);
    ~OAIBurnTokenResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<double> getMultisigOutputs() const;
    void setMultisigOutputs(const QList<double> &multisig_outputs);
    bool is_multisig_outputs_Set() const;
    bool is_multisig_outputs_Valid() const;

    QList<double> getNtp1OutputIndexes() const;
    void setNtp1OutputIndexes(const QList<double> &ntp1_output_indexes);
    bool is_ntp1_output_indexes_Set() const;
    bool is_ntp1_output_indexes_Valid() const;

    QString getTxHex() const;
    void setTxHex(const QString &tx_hex);
    bool is_tx_hex_Set() const;
    bool is_tx_hex_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<double> m_multisig_outputs;
    bool m_multisig_outputs_isSet;
    bool m_multisig_outputs_isValid;

    QList<double> m_ntp1_output_indexes;
    bool m_ntp1_output_indexes_isSet;
    bool m_ntp1_output_indexes_isValid;

    QString m_tx_hex;
    bool m_tx_hex_isSet;
    bool m_tx_hex_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBurnTokenResponse)

#endif // OAIBurnTokenResponse_H
