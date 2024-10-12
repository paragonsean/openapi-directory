/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFileUploadResponse_details.h
 *
 * 
 */

#ifndef OAIFileUploadResponse_details_H
#define OAIFileUploadResponse_details_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFileUploadResponse_details : public OAIObject {
public:
    OAIFileUploadResponse_details();
    OAIFileUploadResponse_details(QString json);
    ~OAIFileUploadResponse_details() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getPath() const;
    void setPath(const QString &path);
    bool is_path_Set() const;
    bool is_path_Valid() const;

    QString getSize() const;
    void setSize(const QString &size);
    bool is_size_Set() const;
    bool is_size_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_path;
    bool m_path_isSet;
    bool m_path_isValid;

    QString m_size;
    bool m_size_isSet;
    bool m_size_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFileUploadResponse_details)

#endif // OAIFileUploadResponse_details_H
