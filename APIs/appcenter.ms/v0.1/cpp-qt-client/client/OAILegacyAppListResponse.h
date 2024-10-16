/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAILegacyAppListResponse.h
 *
 * 
 */

#ifndef OAILegacyAppListResponse_H
#define OAILegacyAppListResponse_H

#include <QJsonObject>

#include "OAILegacyAppListResponse_apps_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILegacyAppListResponse_apps_inner;

class OAILegacyAppListResponse : public OAIObject {
public:
    OAILegacyAppListResponse();
    OAILegacyAppListResponse(QString json);
    ~OAILegacyAppListResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAILegacyAppListResponse_apps_inner> getApps() const;
    void setApps(const QList<OAILegacyAppListResponse_apps_inner> &apps);
    bool is_apps_Set() const;
    bool is_apps_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAILegacyAppListResponse_apps_inner> m_apps;
    bool m_apps_isSet;
    bool m_apps_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILegacyAppListResponse)

#endif // OAILegacyAppListResponse_H
