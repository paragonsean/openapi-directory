/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIListSiteIdentifiersAssignedToHostName_request.h
 *
 * Identifies an object.
 */

#ifndef OAIListSiteIdentifiersAssignedToHostName_request_H
#define OAIListSiteIdentifiersAssignedToHostName_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIListSiteIdentifiersAssignedToHostName_request : public OAIObject {
public:
    OAIListSiteIdentifiersAssignedToHostName_request();
    OAIListSiteIdentifiersAssignedToHostName_request(QString json);
    ~OAIListSiteIdentifiersAssignedToHostName_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIListSiteIdentifiersAssignedToHostName_request)

#endif // OAIListSiteIdentifiersAssignedToHostName_request_H
