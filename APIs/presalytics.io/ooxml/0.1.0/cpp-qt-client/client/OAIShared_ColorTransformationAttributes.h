/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIShared_ColorTransformationAttributes.h
 *
 * 
 */

#ifndef OAIShared_ColorTransformationAttributes_H
#define OAIShared_ColorTransformationAttributes_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIShared_ColorTransformationAttributes : public OAIObject {
public:
    OAIShared_ColorTransformationAttributes();
    OAIShared_ColorTransformationAttributes(QString json);
    ~OAIShared_ColorTransformationAttributes() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getColorTransformationsId() const;
    void setColorTransformationsId(const QString &color_transformations_id);
    bool is_color_transformations_id_Set() const;
    bool is_color_transformations_id_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getValue() const;
    void setValue(const QString &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_color_transformations_id;
    bool m_color_transformations_id_isSet;
    bool m_color_transformations_id_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIShared_ColorTransformationAttributes)

#endif // OAIShared_ColorTransformationAttributes_H
