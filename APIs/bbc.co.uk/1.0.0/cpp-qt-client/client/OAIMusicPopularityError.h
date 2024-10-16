/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIMusicPopularityError.h
 *
 * 
 */

#ifndef OAIMusicPopularityError_H
#define OAIMusicPopularityError_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIMusicPopularityError : public OAIObject {
public:
    OAIMusicPopularityError();
    OAIMusicPopularityError(QString json);
    ~OAIMusicPopularityError() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getErrors() const;
    void setErrors(const QList<QString> &errors);
    bool is_errors_Set() const;
    bool is_errors_Valid() const;

    QString getSchema() const;
    void setSchema(const QString &schema);
    bool is_schema_Set() const;
    bool is_schema_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_errors;
    bool m_errors_isSet;
    bool m_errors_isValid;

    QString m_schema;
    bool m_schema_isSet;
    bool m_schema_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIMusicPopularityError)

#endif // OAIMusicPopularityError_H
