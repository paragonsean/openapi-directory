/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDeployment.h
 *
 * 
 */

#ifndef OAIDeployment_H
#define OAIDeployment_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDeployment : public OAIObject {
public:
    OAIDeployment();
    OAIDeployment(QString json);
    ~OAIDeployment() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getHttpUrl() const;
    void setHttpUrl(const QString &http_url);
    bool is_http_url_Set() const;
    bool is_http_url_Valid() const;

    QString getRepoState() const;
    void setRepoState(const QString &repo_state);
    bool is_repo_state_Set() const;
    bool is_repo_state_Valid() const;

    bool isShutdownable() const;
    void setShutdownable(const bool &shutdownable);
    bool is_shutdownable_Set() const;
    bool is_shutdownable_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_http_url;
    bool m_http_url_isSet;
    bool m_http_url_isValid;

    QString m_repo_state;
    bool m_repo_state_isSet;
    bool m_repo_state_isValid;

    bool m_shutdownable;
    bool m_shutdownable_isSet;
    bool m_shutdownable_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDeployment)

#endif // OAIDeployment_H
