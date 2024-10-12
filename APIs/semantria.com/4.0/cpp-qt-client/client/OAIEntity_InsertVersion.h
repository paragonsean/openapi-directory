/**
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEntity_InsertVersion.h
 *
 * 
 */

#ifndef OAIEntity_InsertVersion_H
#define OAIEntity_InsertVersion_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIEntity_InsertVersion : public OAIObject {
public:
    OAIEntity_InsertVersion();
    OAIEntity_InsertVersion(QString json);
    ~OAIEntity_InsertVersion() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getLabel() const;
    void setLabel(const QString &label);
    bool is_label_Set() const;
    bool is_label_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getNormalized() const;
    void setNormalized(const QString &normalized);
    bool is_normalized_Set() const;
    bool is_normalized_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_label;
    bool m_label_isSet;
    bool m_label_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_normalized;
    bool m_normalized_isSet;
    bool m_normalized_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEntity_InsertVersion)

#endif // OAIEntity_InsertVersion_H
