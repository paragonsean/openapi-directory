/**
 * Request Baskets API
 * RESTful API of [Request Baskets](https://rbaskets.in) service.  Request Baskets is an open source project of a service to collect HTTP requests and inspect them via RESTful API or web UI.  Check out the [project page](https://github.com/darklynx/request-baskets) for more detailed description. 
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIVersion.h
 *
 * 
 */

#ifndef OAIVersion_H
#define OAIVersion_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIVersion : public OAIObject {
public:
    OAIVersion();
    OAIVersion(QString json);
    ~OAIVersion() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCommit() const;
    void setCommit(const QString &commit);
    bool is_commit_Set() const;
    bool is_commit_Valid() const;

    QString getCommitShort() const;
    void setCommitShort(const QString &commit_short);
    bool is_commit_short_Set() const;
    bool is_commit_short_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getSourceCode() const;
    void setSourceCode(const QString &source_code);
    bool is_source_code_Set() const;
    bool is_source_code_Valid() const;

    QString getVersion() const;
    void setVersion(const QString &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_commit;
    bool m_commit_isSet;
    bool m_commit_isValid;

    QString m_commit_short;
    bool m_commit_short_isSet;
    bool m_commit_short_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_source_code;
    bool m_source_code_isSet;
    bool m_source_code_isValid;

    QString m_version;
    bool m_version_isSet;
    bool m_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVersion)

#endif // OAIVersion_H
