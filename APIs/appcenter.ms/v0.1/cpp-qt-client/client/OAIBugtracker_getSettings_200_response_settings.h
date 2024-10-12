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
 * OAIBugtracker_getSettings_200_response_settings.h
 *
 * Bugtracker specific settings
 */

#ifndef OAIBugtracker_getSettings_200_response_settings_H
#define OAIBugtracker_getSettings_200_response_settings_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBugtracker_getSettings_200_response_settings : public OAIObject {
public:
    OAIBugtracker_getSettings_200_response_settings();
    OAIBugtracker_getSettings_200_response_settings(QString json);
    ~OAIBugtracker_getSettings_200_response_settings() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCallbackUrl() const;
    void setCallbackUrl(const QString &callback_url);
    bool is_callback_url_Set() const;
    bool is_callback_url_Valid() const;

    QString getOwnerName() const;
    void setOwnerName(const QString &owner_name);
    bool is_owner_name_Set() const;
    bool is_owner_name_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_callback_url;
    bool m_callback_url_isSet;
    bool m_callback_url_isValid;

    QString m_owner_name;
    bool m_owner_name_isSet;
    bool m_owner_name_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBugtracker_getSettings_200_response_settings)

#endif // OAIBugtracker_getSettings_200_response_settings_H
