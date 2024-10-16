/**
 * Cenit IO - REST API Specification
 * Cenit IO is an Open Platform for Data and Business Integration (iPaaS) 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@cenit.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIScheduler.h
 *
 * 
 */

#ifndef OAIScheduler_H
#define OAIScheduler_H

#include <QJsonObject>

#include "OAINamespace.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAINamespace;

class OAIScheduler : public OAIObject {
public:
    OAIScheduler();
    OAIScheduler(QString json);
    ~OAIScheduler() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isActivated() const;
    void setActivated(const bool &activated);
    bool is_activated_Set() const;
    bool is_activated_Valid() const;

    QString getExpression() const;
    void setExpression(const QString &expression);
    bool is_expression_Set() const;
    bool is_expression_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    OAINamespace getRNamespace() const;
    void setRNamespace(const OAINamespace &r_namespace);
    bool is_r_namespace_Set() const;
    bool is_r_namespace_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_activated;
    bool m_activated_isSet;
    bool m_activated_isValid;

    QString m_expression;
    bool m_expression_isSet;
    bool m_expression_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    OAINamespace m_r_namespace;
    bool m_r_namespace_isSet;
    bool m_r_namespace_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIScheduler)

#endif // OAIScheduler_H
