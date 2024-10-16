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
 * OAIIssueTokenRequest_metadata_rules_holders_inner.h
 *
 * 
 */

#ifndef OAIIssueTokenRequest_metadata_rules_holders_inner_H
#define OAIIssueTokenRequest_metadata_rules_holders_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIIssueTokenRequest_metadata_rules_holders_inner : public OAIObject {
public:
    OAIIssueTokenRequest_metadata_rules_holders_inner();
    OAIIssueTokenRequest_metadata_rules_holders_inner(QString json);
    ~OAIIssueTokenRequest_metadata_rules_holders_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAddress() const;
    void setAddress(const QString &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    bool isLocked() const;
    void setLocked(const bool &locked);
    bool is_locked_Set() const;
    bool is_locked_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    bool m_locked;
    bool m_locked_isSet;
    bool m_locked_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIssueTokenRequest_metadata_rules_holders_inner)

#endif // OAIIssueTokenRequest_metadata_rules_holders_inner_H
