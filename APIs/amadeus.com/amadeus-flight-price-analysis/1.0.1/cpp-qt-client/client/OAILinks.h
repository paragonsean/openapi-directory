/**
 * Flight Price Analysis API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAILinks.h
 *
 * Links related to the returned objects(s)
 */

#ifndef OAILinks_H
#define OAILinks_H

#include <QJsonObject>

#include <QList>
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

    QString getHref() const;
    void setHref(const QString &href);
    bool is_href_Set() const;
    bool is_href_Valid() const;

    QList<QString> getMethods() const;
    void setMethods(const QList<QString> &methods);
    bool is_methods_Set() const;
    bool is_methods_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_href;
    bool m_href_isSet;
    bool m_href_isValid;

    QList<QString> m_methods;
    bool m_methods_isSet;
    bool m_methods_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILinks)

#endif // OAILinks_H
