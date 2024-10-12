/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIResourceNameAvailabilityRequest.h
 *
 * Resource name availability request content.
 */

#ifndef OAIResourceNameAvailabilityRequest_H
#define OAIResourceNameAvailabilityRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIResourceNameAvailabilityRequest : public OAIObject {
public:
    OAIResourceNameAvailabilityRequest();
    OAIResourceNameAvailabilityRequest(QString json);
    ~OAIResourceNameAvailabilityRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isIsFqdn() const;
    void setIsFqdn(const bool &is_fqdn);
    bool is_is_fqdn_Set() const;
    bool is_is_fqdn_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_is_fqdn;
    bool m_is_fqdn_isSet;
    bool m_is_fqdn_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIResourceNameAvailabilityRequest)

#endif // OAIResourceNameAvailabilityRequest_H
