/**
 * Story
 * This API is the main entry point for creating, editing and publishing analytics throught the Presalytics API
 *
 * The version of the OpenAPI document: 0.3.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFile_upload.h
 *
 * A Base64 encoded file object
 */

#ifndef OAIFile_upload_H
#define OAIFile_upload_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFile_upload : public OAIObject {
public:
    OAIFile_upload();
    OAIFile_upload(QString json);
    ~OAIFile_upload() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getContentLength() const;
    void setContentLength(const qint32 &content_length);
    bool is_content_length_Set() const;
    bool is_content_length_Valid() const;

    QString getFile() const;
    void setFile(const QString &file);
    bool is_file_Set() const;
    bool is_file_Valid() const;

    QString getFileName() const;
    void setFileName(const QString &file_name);
    bool is_file_name_Set() const;
    bool is_file_name_Valid() const;

    QString getMimetype() const;
    void setMimetype(const QString &mimetype);
    bool is_mimetype_Set() const;
    bool is_mimetype_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_content_length;
    bool m_content_length_isSet;
    bool m_content_length_isValid;

    QString m_file;
    bool m_file_isSet;
    bool m_file_isValid;

    QString m_file_name;
    bool m_file_name_isSet;
    bool m_file_name_isValid;

    QString m_mimetype;
    bool m_mimetype_isSet;
    bool m_mimetype_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFile_upload)

#endif // OAIFile_upload_H
