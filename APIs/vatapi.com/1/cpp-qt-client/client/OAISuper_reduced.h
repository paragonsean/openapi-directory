/**
 * VAT API
 * A developer friendly API to help your business achieve VAT compliance
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISuper_reduced.h
 *
 * 
 */

#ifndef OAISuper_reduced_H
#define OAISuper_reduced_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISuper_reduced : public OAIObject {
public:
    OAISuper_reduced();
    OAISuper_reduced(QString json);
    ~OAISuper_reduced() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAppliesTo() const;
    void setAppliesTo(const QString &applies_to);
    bool is_applies_to_Set() const;
    bool is_applies_to_Valid() const;

    qint32 getValue() const;
    void setValue(const qint32 &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_applies_to;
    bool m_applies_to_isSet;
    bool m_applies_to_isValid;

    qint32 m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISuper_reduced)

#endif // OAISuper_reduced_H
