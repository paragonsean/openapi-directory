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
 * OAISample_1.h
 *
 * 
 */

#ifndef OAISample_1_H
#define OAISample_1_H

#include <QJsonObject>

#include "OAISample_1_items_inner.h"
#include <QSet>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISample_1_items_inner;

class OAISample_1 : public OAIObject {
public:
    OAISample_1();
    OAISample_1(QString json);
    ~OAISample_1() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDirectory() const;
    void setDirectory(const QString &directory);
    bool is_directory_Set() const;
    bool is_directory_Valid() const;

    QSet<OAISample_1_items_inner> getItems() const;
    void setItems(const QSet<OAISample_1_items_inner> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_directory;
    bool m_directory_isSet;
    bool m_directory_isValid;

    QSet<OAISample_1_items_inner> m_items;
    bool m_items_isSet;
    bool m_items_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISample_1)

#endif // OAISample_1_H
