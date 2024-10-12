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
 * OAIGet_List_of_issued_Documents_id_200_response.h
 *
 * 
 */

#ifndef OAIGet_List_of_issued_Documents_id_200_response_H
#define OAIGet_List_of_issued_Documents_id_200_response_H

#include <QJsonObject>

#include "OAIGet_List_of_issued_Documents_id_200_response_items_inner.h"
#include <QSet>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGet_List_of_issued_Documents_id_200_response_items_inner;

class OAIGet_List_of_issued_Documents_id_200_response : public OAIObject {
public:
    OAIGet_List_of_issued_Documents_id_200_response();
    OAIGet_List_of_issued_Documents_id_200_response(QString json);
    ~OAIGet_List_of_issued_Documents_id_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QSet<OAIGet_List_of_issued_Documents_id_200_response_items_inner> getItems() const;
    void setItems(const QSet<OAIGet_List_of_issued_Documents_id_200_response_items_inner> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    QString getResource() const;
    void setResource(const QString &resource);
    bool is_resource_Set() const;
    bool is_resource_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QSet<OAIGet_List_of_issued_Documents_id_200_response_items_inner> m_items;
    bool m_items_isSet;
    bool m_items_isValid;

    QString m_resource;
    bool m_resource_isSet;
    bool m_resource_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGet_List_of_issued_Documents_id_200_response)

#endif // OAIGet_List_of_issued_Documents_id_200_response_H
