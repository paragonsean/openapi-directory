/**
 * Azure SQL Database Import/Export spec
 * Provides create and read functionality for Import/Export operations on Azure SQL databases.
 *
 * The version of the OpenAPI document: 2014-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIImportRequest.h
 *
 * Import database parameters.
 */

#ifndef OAIImportRequest_H
#define OAIImportRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIImportRequest : public OAIObject {
public:
    OAIImportRequest();
    OAIImportRequest(QString json);
    ~OAIImportRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDatabaseName() const;
    void setDatabaseName(const QString &database_name);
    bool is_database_name_Set() const;
    bool is_database_name_Valid() const;

    QString getEdition() const;
    void setEdition(const QString &edition);
    bool is_edition_Set() const;
    bool is_edition_Valid() const;

    QString getMaxSizeBytes() const;
    void setMaxSizeBytes(const QString &max_size_bytes);
    bool is_max_size_bytes_Set() const;
    bool is_max_size_bytes_Valid() const;

    QString getServiceObjectiveName() const;
    void setServiceObjectiveName(const QString &service_objective_name);
    bool is_service_objective_name_Set() const;
    bool is_service_objective_name_Valid() const;

    QString getAdministratorLogin() const;
    void setAdministratorLogin(const QString &administrator_login);
    bool is_administrator_login_Set() const;
    bool is_administrator_login_Valid() const;

    QString getAdministratorLoginPassword() const;
    void setAdministratorLoginPassword(const QString &administrator_login_password);
    bool is_administrator_login_password_Set() const;
    bool is_administrator_login_password_Valid() const;

    QString getAuthenticationType() const;
    void setAuthenticationType(const QString &authentication_type);
    bool is_authentication_type_Set() const;
    bool is_authentication_type_Valid() const;

    QString getStorageKey() const;
    void setStorageKey(const QString &storage_key);
    bool is_storage_key_Set() const;
    bool is_storage_key_Valid() const;

    QString getStorageKeyType() const;
    void setStorageKeyType(const QString &storage_key_type);
    bool is_storage_key_type_Set() const;
    bool is_storage_key_type_Valid() const;

    QString getStorageUri() const;
    void setStorageUri(const QString &storage_uri);
    bool is_storage_uri_Set() const;
    bool is_storage_uri_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_database_name;
    bool m_database_name_isSet;
    bool m_database_name_isValid;

    QString m_edition;
    bool m_edition_isSet;
    bool m_edition_isValid;

    QString m_max_size_bytes;
    bool m_max_size_bytes_isSet;
    bool m_max_size_bytes_isValid;

    QString m_service_objective_name;
    bool m_service_objective_name_isSet;
    bool m_service_objective_name_isValid;

    QString m_administrator_login;
    bool m_administrator_login_isSet;
    bool m_administrator_login_isValid;

    QString m_administrator_login_password;
    bool m_administrator_login_password_isSet;
    bool m_administrator_login_password_isValid;

    QString m_authentication_type;
    bool m_authentication_type_isSet;
    bool m_authentication_type_isValid;

    QString m_storage_key;
    bool m_storage_key_isSet;
    bool m_storage_key_isValid;

    QString m_storage_key_type;
    bool m_storage_key_type_isSet;
    bool m_storage_key_type_isValid;

    QString m_storage_uri;
    bool m_storage_uri_isSet;
    bool m_storage_uri_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImportRequest)

#endif // OAIImportRequest_H
