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
 * OAIAvailableAppBuilds.h
 *
 * 
 */

#ifndef OAIAvailableAppBuilds_H
#define OAIAvailableAppBuilds_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAvailableAppBuilds : public OAIObject {
public:
    OAIAvailableAppBuilds();
    OAIAvailableAppBuilds(QString json);
    ~OAIAvailableAppBuilds() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getAppBuilds() const;
    void setAppBuilds(const QList<QString> &app_builds);
    bool is_app_builds_Set() const;
    bool is_app_builds_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_app_builds;
    bool m_app_builds_isSet;
    bool m_app_builds_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAvailableAppBuilds)

#endif // OAIAvailableAppBuilds_H
