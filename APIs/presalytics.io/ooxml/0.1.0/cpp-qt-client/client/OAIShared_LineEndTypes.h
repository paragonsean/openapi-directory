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
 * OAIShared_LineEndTypes.h
 *
 * 
 */

#ifndef OAIShared_LineEndTypes_H
#define OAIShared_LineEndTypes_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIShared_LineEndTypes : public OAIObject {
public:
    OAIShared_LineEndTypes();
    OAIShared_LineEndTypes(QString json);
    ~OAIShared_LineEndTypes() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getSerializedAs() const;
    void setSerializedAs(const QString &serialized_as);
    bool is_serialized_as_Set() const;
    bool is_serialized_as_Valid() const;

    qint32 getTypeId() const;
    void setTypeId(const qint32 &type_id);
    bool is_type_id_Set() const;
    bool is_type_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_serialized_as;
    bool m_serialized_as_isSet;
    bool m_serialized_as_isValid;

    qint32 m_type_id;
    bool m_type_id_isSet;
    bool m_type_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIShared_LineEndTypes)

#endif // OAIShared_LineEndTypes_H
