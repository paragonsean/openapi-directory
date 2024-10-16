/**
 * PdfBroker.io API
 * PdfBroker.io is an api for creating pdf files from Xsl-Fo or Html and other useful pdf utilities.
 *
 * The version of the OpenAPI document: v1
 * Contact: support@pdfbroker.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFontDto.h
 *
 * The Font dto object
 */

#ifndef OAIFontDto_H
#define OAIFontDto_H

#include <QJsonObject>

#include "OAIFontStyle.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFontDto : public OAIObject {
public:
    OAIFontDto();
    OAIFontDto(QString json);
    ~OAIFontDto() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    float getSize() const;
    void setSize(const float &size);
    bool is_size_Set() const;
    bool is_size_Valid() const;

    OAIFontStyle getStyle() const;
    void setStyle(const OAIFontStyle &style);
    bool is_style_Set() const;
    bool is_style_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    float m_size;
    bool m_size_isSet;
    bool m_size_isValid;

    OAIFontStyle m_style;
    bool m_style_isSet;
    bool m_style_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFontDto)

#endif // OAIFontDto_H
