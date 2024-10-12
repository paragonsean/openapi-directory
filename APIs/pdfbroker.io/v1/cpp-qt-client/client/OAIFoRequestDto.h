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
 * OAIFoRequestDto.h
 *
 * The basic request with the XSL-FO document as a Base64 encoded string with a set of resources provided with a name and the data of the resource as a Base64 encoded string.
 */

#ifndef OAIFoRequestDto_H
#define OAIFoRequestDto_H

#include <QJsonObject>

#include "OAIPdfMetadataDto.h"
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPdfMetadataDto;

class OAIFoRequestDto : public OAIObject {
public:
    OAIFoRequestDto();
    OAIFoRequestDto(QString json);
    ~OAIFoRequestDto() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getFoDocumentBase64String() const;
    void setFoDocumentBase64String(const QString &fo_document_base64_string);
    bool is_fo_document_base64_string_Set() const;
    bool is_fo_document_base64_string_Valid() const;

    OAIPdfMetadataDto getMetadata() const;
    void setMetadata(const OAIPdfMetadataDto &metadata);
    bool is_metadata_Set() const;
    bool is_metadata_Valid() const;

    QMap<QString, QString> getResources() const;
    void setResources(const QMap<QString, QString> &resources);
    bool is_resources_Set() const;
    bool is_resources_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_fo_document_base64_string;
    bool m_fo_document_base64_string_isSet;
    bool m_fo_document_base64_string_isValid;

    OAIPdfMetadataDto m_metadata;
    bool m_metadata_isSet;
    bool m_metadata_isValid;

    QMap<QString, QString> m_resources;
    bool m_resources_isSet;
    bool m_resources_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFoRequestDto)

#endif // OAIFoRequestDto_H
