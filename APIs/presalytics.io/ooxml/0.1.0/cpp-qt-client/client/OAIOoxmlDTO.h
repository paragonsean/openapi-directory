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
 * OAIOoxmlDTO.h
 *
 * 
 */

#ifndef OAIOoxmlDTO_H
#define OAIOoxmlDTO_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIOoxmlDTO : public OAIObject {
public:
    OAIOoxmlDTO();
    OAIOoxmlDTO(QString json);
    ~OAIOoxmlDTO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getOpenOfficeXml() const;
    void setOpenOfficeXml(const QString &open_office_xml);
    bool is_open_office_xml_Set() const;
    bool is_open_office_xml_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_open_office_xml;
    bool m_open_office_xml_isSet;
    bool m_open_office_xml_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOoxmlDTO)

#endif // OAIOoxmlDTO_H
