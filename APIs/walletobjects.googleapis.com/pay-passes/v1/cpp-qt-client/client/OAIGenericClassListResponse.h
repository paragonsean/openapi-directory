/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGenericClassListResponse.h
 *
 * List response which contains the list of all generic classes for a given issuer ID.
 */

#ifndef OAIGenericClassListResponse_H
#define OAIGenericClassListResponse_H

#include <QJsonObject>

#include "OAIGenericClass.h"
#include "OAIPagination.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPagination;
class OAIGenericClass;

class OAIGenericClassListResponse : public OAIObject {
public:
    OAIGenericClassListResponse();
    OAIGenericClassListResponse(QString json);
    ~OAIGenericClassListResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPagination getPagination() const;
    void setPagination(const OAIPagination &pagination);
    bool is_pagination_Set() const;
    bool is_pagination_Valid() const;

    QList<OAIGenericClass> getResources() const;
    void setResources(const QList<OAIGenericClass> &resources);
    bool is_resources_Set() const;
    bool is_resources_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIPagination m_pagination;
    bool m_pagination_isSet;
    bool m_pagination_isValid;

    QList<OAIGenericClass> m_resources;
    bool m_resources_isSet;
    bool m_resources_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGenericClassListResponse)

#endif // OAIGenericClassListResponse_H
