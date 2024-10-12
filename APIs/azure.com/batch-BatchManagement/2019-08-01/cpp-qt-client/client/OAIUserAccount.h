/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUserAccount.h
 *
 * 
 */

#ifndef OAIUserAccount_H
#define OAIUserAccount_H

#include <QJsonObject>

#include "OAIElevationLevel.h"
#include "OAILinuxUserConfiguration.h"
#include "OAIWindowsUserConfiguration.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILinuxUserConfiguration;
class OAIWindowsUserConfiguration;

class OAIUserAccount : public OAIObject {
public:
    OAIUserAccount();
    OAIUserAccount(QString json);
    ~OAIUserAccount() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIElevationLevel getElevationLevel() const;
    void setElevationLevel(const OAIElevationLevel &elevation_level);
    bool is_elevation_level_Set() const;
    bool is_elevation_level_Valid() const;

    OAILinuxUserConfiguration getLinuxUserConfiguration() const;
    void setLinuxUserConfiguration(const OAILinuxUserConfiguration &linux_user_configuration);
    bool is_linux_user_configuration_Set() const;
    bool is_linux_user_configuration_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    OAIWindowsUserConfiguration getWindowsUserConfiguration() const;
    void setWindowsUserConfiguration(const OAIWindowsUserConfiguration &windows_user_configuration);
    bool is_windows_user_configuration_Set() const;
    bool is_windows_user_configuration_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIElevationLevel m_elevation_level;
    bool m_elevation_level_isSet;
    bool m_elevation_level_isValid;

    OAILinuxUserConfiguration m_linux_user_configuration;
    bool m_linux_user_configuration_isSet;
    bool m_linux_user_configuration_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    OAIWindowsUserConfiguration m_windows_user_configuration;
    bool m_windows_user_configuration_isSet;
    bool m_windows_user_configuration_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUserAccount)

#endif // OAIUserAccount_H
