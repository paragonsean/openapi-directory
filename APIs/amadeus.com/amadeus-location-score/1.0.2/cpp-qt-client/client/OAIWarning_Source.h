/**
 * Location Score
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.     Please also be aware that our test environment is based on a subset of the production, this API in test only returns a few selected cities. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIWarning_Source.h
 *
 * The Warning Source Definition
 */

#ifndef OAIWarning_Source_H
#define OAIWarning_Source_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIWarning_Source : public OAIObject {
public:
    OAIWarning_Source();
    OAIWarning_Source(QString json);
    ~OAIWarning_Source() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getExample() const;
    void setExample(const QString &example);
    bool is_example_Set() const;
    bool is_example_Valid() const;

    QString getParameter() const;
    void setParameter(const QString &parameter);
    bool is_parameter_Set() const;
    bool is_parameter_Valid() const;

    QString getPointer() const;
    void setPointer(const QString &pointer);
    bool is_pointer_Set() const;
    bool is_pointer_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_example;
    bool m_example_isSet;
    bool m_example_isValid;

    QString m_parameter;
    bool m_parameter_isSet;
    bool m_parameter_isValid;

    QString m_pointer;
    bool m_pointer_isSet;
    bool m_pointer_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWarning_Source)

#endif // OAIWarning_Source_H
