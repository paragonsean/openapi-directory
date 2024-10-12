/**
 * Airport On-Time Performance
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.0.4
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAILinks.h
 *
 * 
 */

#ifndef OAILinks_H
#define OAILinks_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAILinks : public OAIObject {
public:
    OAILinks();
    OAILinks(QString json);
    ~OAILinks() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getRelated() const;
    void setRelated(const QString &related);
    bool is_related_Set() const;
    bool is_related_Valid() const;

    QString getSelf() const;
    void setSelf(const QString &self);
    bool is_self_Set() const;
    bool is_self_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_related;
    bool m_related_isSet;
    bool m_related_isValid;

    QString m_self;
    bool m_self_isSet;
    bool m_self_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILinks)

#endif // OAILinks_H
