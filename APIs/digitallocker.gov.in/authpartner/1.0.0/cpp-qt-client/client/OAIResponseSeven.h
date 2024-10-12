/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIResponseSeven.h
 *
 * 
 */

#ifndef OAIResponseSeven_H
#define OAIResponseSeven_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIResponseSeven : public OAIObject {
public:
    OAIResponseSeven();
    OAIResponseSeven(QString json);
    ~OAIResponseSeven() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getError() const;
    void setError(const QString &error);
    bool is_error_Set() const;
    bool is_error_Valid() const;

    QString getErrorDescription() const;
    void setErrorDescription(const QString &error_description);
    bool is_error_description_Set() const;
    bool is_error_description_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_error;
    bool m_error_isSet;
    bool m_error_isValid;

    QString m_error_description;
    bool m_error_description_isSet;
    bool m_error_description_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIResponseSeven)

#endif // OAIResponseSeven_H
