/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITest_Cloud_Hash_Upload_Status.h
 *
 * Status of the upload
 */

#ifndef OAITest_Cloud_Hash_Upload_Status_H
#define OAITest_Cloud_Hash_Upload_Status_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITest_Cloud_Hash_Upload_Status : public OAIObject {
public:
    OAITest_Cloud_Hash_Upload_Status();
    OAITest_Cloud_Hash_Upload_Status(QString json);
    ~OAITest_Cloud_Hash_Upload_Status() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getLocation() const;
    void setLocation(const QString &location);
    bool is_location_Set() const;
    bool is_location_Valid() const;

    double getStatusCode() const;
    void setStatusCode(const double &status_code);
    bool is_status_code_Set() const;
    bool is_status_code_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_location;
    bool m_location_isSet;
    bool m_location_isValid;

    double m_status_code;
    bool m_status_code_isSet;
    bool m_status_code_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITest_Cloud_Hash_Upload_Status)

#endif // OAITest_Cloud_Hash_Upload_Status_H
