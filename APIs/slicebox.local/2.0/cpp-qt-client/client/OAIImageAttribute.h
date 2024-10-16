/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIImageAttribute.h
 *
 * 
 */

#ifndef OAIImageAttribute_H
#define OAIImageAttribute_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIImageAttribute : public OAIObject {
public:
    OAIImageAttribute();
    OAIImageAttribute(QString json);
    ~OAIImageAttribute() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getDepth() const;
    void setDepth(const qint32 &depth);
    bool is_depth_Set() const;
    bool is_depth_Valid() const;

    QString getElement() const;
    void setElement(const QString &element);
    bool is_element_Set() const;
    bool is_element_Valid() const;

    QString getGroup() const;
    void setGroup(const QString &group);
    bool is_group_Set() const;
    bool is_group_Valid() const;

    qint32 getLength() const;
    void setLength(const qint32 &length);
    bool is_length_Set() const;
    bool is_length_Valid() const;

    qint32 getMultiplicity() const;
    void setMultiplicity(const qint32 &multiplicity);
    bool is_multiplicity_Set() const;
    bool is_multiplicity_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getPath() const;
    void setPath(const QString &path);
    bool is_path_Set() const;
    bool is_path_Valid() const;

    QString getValue() const;
    void setValue(const QString &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    QString getVr() const;
    void setVr(const QString &vr);
    bool is_vr_Set() const;
    bool is_vr_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_depth;
    bool m_depth_isSet;
    bool m_depth_isValid;

    QString m_element;
    bool m_element_isSet;
    bool m_element_isValid;

    QString m_group;
    bool m_group_isSet;
    bool m_group_isValid;

    qint32 m_length;
    bool m_length_isSet;
    bool m_length_isValid;

    qint32 m_multiplicity;
    bool m_multiplicity_isSet;
    bool m_multiplicity_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_path;
    bool m_path_isSet;
    bool m_path_isValid;

    QString m_value;
    bool m_value_isSet;
    bool m_value_isValid;

    QString m_vr;
    bool m_vr_isSet;
    bool m_vr_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImageAttribute)

#endif // OAIImageAttribute_H
