/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIMeta.h
 *
 * 
 */

#ifndef OAIMeta_H
#define OAIMeta_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIMeta : public OAIObject {
public:
    OAIMeta();
    OAIMeta(QString json);
    ~OAIMeta() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCommunicationExpiry() const;
    void setCommunicationExpiry(const QString &communication_expiry);
    bool is_communication_expiry_Set() const;
    bool is_communication_expiry_Valid() const;

    QString getCommunicationHint() const;
    void setCommunicationHint(const QString &communication_hint);
    bool is_communication_hint_Set() const;
    bool is_communication_hint_Valid() const;

    QString getCommunicationMedium() const;
    void setCommunicationMedium(const QString &communication_medium);
    bool is_communication_medium_Set() const;
    bool is_communication_medium_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_communication_expiry;
    bool m_communication_expiry_isSet;
    bool m_communication_expiry_isValid;

    QString m_communication_hint;
    bool m_communication_hint_isSet;
    bool m_communication_hint_isValid;

    QString m_communication_medium;
    bool m_communication_medium_isSet;
    bool m_communication_medium_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIMeta)

#endif // OAIMeta_H
