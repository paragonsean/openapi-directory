/**
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOutputFile.h
 *
 * 
 */

#ifndef OAIOutputFile_H
#define OAIOutputFile_H

#include <QJsonObject>

#include "OAIFormat.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIOutputFile : public OAIObject {
public:
    OAIOutputFile();
    OAIOutputFile(QString json);
    ~OAIOutputFile() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getFilename() const;
    void setFilename(const QString &filename);
    bool is_filename_Set() const;
    bool is_filename_Valid() const;

    OAIFormat getFormat() const;
    void setFormat(const OAIFormat &format);
    bool is_format_Set() const;
    bool is_format_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_filename;
    bool m_filename_isSet;
    bool m_filename_isValid;

    OAIFormat m_format;
    bool m_format_isSet;
    bool m_format_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOutputFile)

#endif // OAIOutputFile_H
