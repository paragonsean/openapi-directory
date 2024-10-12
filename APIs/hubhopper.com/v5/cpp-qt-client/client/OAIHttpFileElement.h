/**
 * Hubhopper Partner Integration API(s) - Production
 * This is an interactive document explaining the API(s) that could be used to fetch data from [Hubhopper](https://hubhopper.com). Use the api key provided to authorize `x-api-key` and test the API(s). The output data models are also available for reference.
 *
 * The version of the OpenAPI document: v5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_HTTP_FILE_ELEMENT_H
#define OAI_HTTP_FILE_ELEMENT_H

#include <QJsonValue>
#include <QMetaType>
#include <QString>

namespace OpenAPI {

class OAIHttpFileElement {

public:
    QString variable_name;
    QString local_filename;
    QString request_filename;
    QString mime_type;
    void setMimeType(const QString &mime);
    void setFileName(const QString &name);
    void setVariableName(const QString &name);
    void setRequestFileName(const QString &name);
    bool isSet() const;
    bool fromStringValue(const QString &instr);
    bool fromJsonValue(const QJsonValue &jval);
    bool fromByteArray(const QByteArray &bytes);
    bool saveToFile(const QString &variable_name, const QString &local_filename, const QString &request_filename, const QString &mime, const QByteArray &bytes);
    QString asJson() const;
    QJsonValue asJsonValue() const;
    QByteArray asByteArray() const;
    QByteArray loadFromFile(const QString &variable_name, const QString &local_filename, const QString &request_filename, const QString &mime);
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHttpFileElement)

#endif // OAI_HTTP_FILE_ELEMENT_H
