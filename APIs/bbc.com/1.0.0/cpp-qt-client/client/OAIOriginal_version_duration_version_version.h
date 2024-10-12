/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOriginal_version_duration_version_version.h
 *
 * 
 */

#ifndef OAIOriginal_version_duration_version_version_H
#define OAIOriginal_version_duration_version_version_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIOriginal_version_duration_version_version : public OAIObject {
public:
    OAIOriginal_version_duration_version_version();
    OAIOriginal_version_duration_version_version(QString json);
    ~OAIOriginal_version_duration_version_version() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDuration() const;
    void setDuration(const QString &duration);
    bool is_duration_Set() const;
    bool is_duration_Valid() const;

    QString getHref() const;
    void setHref(const QString &href);
    bool is_href_Set() const;
    bool is_href_Valid() const;

    QString getPid() const;
    void setPid(const QString &pid);
    bool is_pid_Set() const;
    bool is_pid_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_duration;
    bool m_duration_isSet;
    bool m_duration_isValid;

    QString m_href;
    bool m_href_isSet;
    bool m_href_isValid;

    QString m_pid;
    bool m_pid_isSet;
    bool m_pid_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOriginal_version_duration_version_version)

#endif // OAIOriginal_version_duration_version_version_H
