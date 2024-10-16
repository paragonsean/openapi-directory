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
 * OAIAnalytics_Versions_200_response_versions_inner.h
 *
 * 
 */

#ifndef OAIAnalytics_Versions_200_response_versions_inner_H
#define OAIAnalytics_Versions_200_response_versions_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAnalytics_Versions_200_response_versions_inner : public OAIObject {
public:
    OAIAnalytics_Versions_200_response_versions_inner();
    OAIAnalytics_Versions_200_response_versions_inner(QString json);
    ~OAIAnalytics_Versions_200_response_versions_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getCount() const;
    void setCount(const qint64 &count);
    bool is_count_Set() const;
    bool is_count_Valid() const;

    qint64 getPreviousCount() const;
    void setPreviousCount(const qint64 &previous_count);
    bool is_previous_count_Set() const;
    bool is_previous_count_Valid() const;

    QString getVersion() const;
    void setVersion(const QString &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_count;
    bool m_count_isSet;
    bool m_count_isValid;

    qint64 m_previous_count;
    bool m_previous_count_isSet;
    bool m_previous_count_isValid;

    QString m_version;
    bool m_version_isSet;
    bool m_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAnalytics_Versions_200_response_versions_inner)

#endif // OAIAnalytics_Versions_200_response_versions_inner_H
