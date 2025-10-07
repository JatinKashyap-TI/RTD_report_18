from odoo import api, SUPERUSER_ID
from odoo.exceptions import ValidationError



def assign_tags_to_custom_taxes(env):
    Tag = env['account.account.tag']

    special_tag_mappings_all = [

    #===============
    #E2 tags
    #===============


    {"tag": "+E2", "tax_xml": "ti_rtd_report.T8_Standard_Rated_EC_Goods_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"},
    {"tag": "-E2", "tax_xml": "ti_rtd_report.T8_Standard_Rated_EC_Goods_23pct_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "base"},
   
    #===============
    #ES2 tags
    #===============


    {"tag": "+ES2", "tax_xml": "ti_rtd_report.T24_Reduced_rated_purchases_from_suppliers_EC_Services_13_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"},
    {"tag": "-ES2", "tax_xml": "ti_rtd_report.T24_Reduced_rated_purchases_from_suppliers_EC_Services_13_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "base"},
		
		
    # ==============================
    # +VOP Tags
    # ==============================
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T19_RCT_Sales", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T24_Reduced_rated_purchases_from_suppliers_EC_Services_13_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T38_Import_Services_Reverse_Charges", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T60_Import_Services_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T61_Import_Goods_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T46_Zero_Rate_ROW_Import_Resale_Postponed_VAT_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T47_Zero_Rate_ROW_Import_NonResale_Postponed_VAT_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T48_Reduced_Rate_ROW_Import_Resale_Postponed_VAT_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T49_Reduced_Rate_ROW_Import_NonResale_Postponed_VAT_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T8_Standard_Rated_EC_Goods_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T44_Standard_Rate_23pct_ROW_Import_Resale_Postponed_VAT_RC_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T45_Standard_Rate_23pct_ROW_Import_NonResale_Postponed_VAT_RC_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T4_135_Purchases_for_resale_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T18_Exempt_Transactions", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T0_Zero_Rated", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T7_135_purchases_not_for_resale", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T12_9_purchases_not_for_resale", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T6_23pct_Standard_Purchases_Not_For_Resale", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T40_Import_of_Goods_Outside_EU_VAT_Paid_Point_of_Entry", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T21_Reverse_Charges_Reduced_Rate", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T4_135pct_Purchases_for_Resale_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOP", "tax_xml": "ti_rtd_report.T2_23pct_Standard_Rate_Purchase_for_Resale_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},

    # ==============================
    # -VOP Tags
    # ==============================
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T19_RCT_Sales", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T24_Reduced_rated_purchases_from_suppliers_EC_Services_13_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T38_Import_Services_Reverse_Charges", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T60_Import_Services_23pct_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T61_Import_Goods_23pct_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T46_Zero_Rate_ROW_Import_Resale_Postponed_VAT_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T47_Zero_Rate_ROW_Import_NonResale_Postponed_VAT_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T48_Reduced_Rate_ROW_Import_Resale_Postponed_VAT_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T49_Reduced_Rate_ROW_Import_NonResale_Postponed_VAT_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T8_Standard_Rated_EC_Goods_23pct_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T44_Standard_Rate_23pct_ROW_Import_Resale_Postponed_VAT_RC_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T45_Standard_Rate_23pct_ROW_Import_NonResale_Postponed_VAT_RC_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T4_135_Purchases_for_resale_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T18_Exempt_Transactions", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T0_Zero_Rated", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T7_135_purchases_not_for_resale", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T12_9_purchases_not_for_resale", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T6_23pct_Standard_Purchases_Not_For_Resale", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T40_Import_of_Goods_Outside_EU_VAT_Paid_Point_of_Entry", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T21_Reverse_Charges_Reduced_Rate", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T4_135pct_Purchases_for_Resale_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOP", "tax_xml": "ti_rtd_report.T2_23pct_Standard_Rate_Purchase_for_Resale_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},

    # ==============================
    # +VOS Tags
    # ==============================
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T18S_Exempt_Sales_Transactions", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T42_Export_of_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T43_Export_of_goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T19_RCT_Sales", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T21_Reverse_Charges_Reduced_Rate", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T3_135_Sales", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T24_Reduced_rated_purchases_from_suppliers_EC_Services_13_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T38_Import_Services_Reverse_Charges", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T1_23pct_Standard_Rate_Sales", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T60_Import_Services_23pct_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T61_Import_Goods_23pct_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T46_Zero_Rate_ROW_Import_Resale_Postponed_VAT_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T47_Zero_Rate_ROW_Import_NonResale_Postponed_VAT_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T48_Reduced_Rate_ROW_Import_Resale_Postponed_VAT_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T49_Reduced_Rate_ROW_Import_NonResale_Postponed_VAT_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T8_Standard_Rated_EC_Goods_23pct_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T44_Standard_Rate_23pct_ROW_Import_Resale_Postponed_VAT_RC_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "+VOS", "tax_xml": "ti_rtd_report.T45_Standard_Rate_23pct_ROW_Import_NonResale_Postponed_VAT_RC_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},

    # ==============================
    # -VOS Tags
    # ==============================
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T18S_Exempt_Sales_Transactions", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T42_Export_of_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T43_Export_of_goods", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T19_RCT_Sales", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T21_Reverse_Charges_Reduced_Rate", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T3_135_Sales", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T24_Reduced_rated_purchases_from_suppliers_EC_Services_13_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T38_Import_Services_Reverse_Charges", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T1_23pct_Standard_Rate_Sales", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T60_Import_Services_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T61_Import_Goods_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T46_Zero_Rate_ROW_Import_Resale_Postponed_VAT_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T47_Zero_Rate_ROW_Import_NonResale_Postponed_VAT_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T48_Reduced_Rate_ROW_Import_Resale_Postponed_VAT_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T49_Reduced_Rate_ROW_Import_NonResale_Postponed_VAT_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T8_Standard_Rated_EC_Goods_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T44_Standard_Rate_23pct_ROW_Import_Resale_Postponed_VAT_RC_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "-VOS", "tax_xml": "ti_rtd_report.T45_Standard_Rate_23pct_ROW_Import_NonResale_Postponed_VAT_RC_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},

    # ==============================
    # +PA1 Tags
    # ==============================
    {"tag": "+PA1", "tax_xml": "ti_rtd_report.T46_Zero_Rate_ROW_Import_Resale_Postponed_VAT_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"},
    {"tag": "+PA1", "tax_xml": "ti_rtd_report.T47_Zero_Rate_ROW_Import_NonResale_Postponed_VAT_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"},
    {"tag": "+PA1", "tax_xml": "ti_rtd_report.T48_Reduced_Rate_ROW_Import_Resale_Postponed_VAT_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"},
    {"tag": "+PA1", "tax_xml": "ti_rtd_report.T49_Reduced_Rate_ROW_Import_NonResale_Postponed_VAT_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"},
    {"tag": "+PA1", "tax_xml": "ti_rtd_report.T44_Standard_Rate_23pct_ROW_Import_Resale_Postponed_VAT_RC_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"},
    {"tag": "+PA1", "tax_xml": "ti_rtd_report.T45_Standard_Rate_23pct_ROW_Import_NonResale_Postponed_VAT_RC_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"},

    # ==============================
    # -PA1 Tags
    # ==============================
    {"tag": "-PA1", "tax_xml": "ti_rtd_report.T46_Zero_Rate_ROW_Import_Resale_Postponed_VAT_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"},
    {"tag": "-PA1", "tax_xml": "ti_rtd_report.T47_Zero_Rate_ROW_Import_NonResale_Postponed_VAT_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"},
    {"tag": "-PA1", "tax_xml": "ti_rtd_report.T48_Reduced_Rate_ROW_Import_Resale_Postponed_VAT_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "base"},
    {"tag": "-PA1", "tax_xml": "ti_rtd_report.T49_Reduced_Rate_ROW_Import_NonResale_Postponed_VAT_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "base"},
    {"tag": "-PA1", "tax_xml": "ti_rtd_report.T44_Standard_Rate_23pct_ROW_Import_Resale_Postponed_VAT_RC_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"},
    {"tag": "-PA1", "tax_xml": "ti_rtd_report.T45_Standard_Rate_23pct_ROW_Import_NonResale_Postponed_VAT_RC_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"},




    {"tag": "+TSVG&S", "tax_xml": "ti_rtd_report.T42_Export_of_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-TSVG&S","tax_xml": "ti_rtd_report.T42_Export_of_Services","line_field": "refund_repartition_line_ids","repartition_type": "tax","factor_percent": 100},
    
    {"tag": "+TSVG&S", "tax_xml": "ti_rtd_report.T43_Export_of_goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-TSVG&S","tax_xml": "ti_rtd_report.T43_Export_of_goods","line_field": "refund_repartition_line_ids","repartition_type": "tax","factor_percent": 100},
    
    {"tag": "+TSVG&S", "tax_xml": "ti_rtd_report.T19_RCT_Sales", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-TSVG&S","tax_xml": "ti_rtd_report.T19_RCT_Sales","line_field": "refund_repartition_line_ids","repartition_type": "tax","factor_percent": 100},
    
    {"tag": "+TSVG&S", "tax_xml": "ti_rtd_report.T21_Reverse_Charges_Reduced_Rate", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-TSVG&S","tax_xml": "ti_rtd_report.T21_Reverse_Charges_Reduced_Rate","line_field": "refund_repartition_line_ids","repartition_type": "tax","factor_percent": 100},
    
    {"tag": "+TSVG&S", "tax_xml": "ti_rtd_report.T3_135_Sales", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-TSVG&S","tax_xml": "ti_rtd_report.T3_135_Sales","line_field": "refund_repartition_line_ids","repartition_type": "tax","factor_percent": 100},
    
    {"tag": "+TSVG&S", "tax_xml": "ti_rtd_report.T38_Import_Services_Reverse_Charges", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "-TSVG&S","tax_xml": "ti_rtd_report.T38_Import_Services_Reverse_Charges","line_field": "refund_repartition_line_ids","repartition_type": "tax","factor_percent": -100},
    
    {"tag": "+TSVG&S", "tax_xml": "ti_rtd_report.T1_23pct_Standard_Rate_Sales", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-TSVG&S","tax_xml": "ti_rtd_report.T1_23pct_Standard_Rate_Sales","line_field": "refund_repartition_line_ids","repartition_type": "tax","factor_percent": 100},
    
    {"tag": "-TSVG&S", "tax_xml": "ti_rtd_report.T60_Import_Services_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "+TSVG&S","tax_xml": "ti_rtd_report.T60_Import_Services_23pct_RC","line_field": "refund_repartition_line_ids","repartition_type": "tax","factor_percent": -100},
    
    {"tag": "-TSVG&S", "tax_xml": "ti_rtd_report.T61_Import_Goods_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": -100},
    {"tag": "+TSVG&S","tax_xml": "ti_rtd_report.T61_Import_Goods_23pct_RC","line_field": "refund_repartition_line_ids","repartition_type": "tax","factor_percent": -100},
    
    
    
    
    {"tag": "+VDEU&PA", "tax_xml": "ti_rtd_report.T46_Zero_Rate_ROW_Import_Resale_Postponed_VAT_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VDEU&PA", "tax_xml": "ti_rtd_report.T47_Zero_Rate_ROW_Import_NonResale_Postponed_VAT_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VDEU&PA", "tax_xml": "ti_rtd_report.T48_Reduced_Rate_ROW_Import_Resale_Postponed_VAT_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VDEU&PA", "tax_xml": "ti_rtd_report.T49_Reduced_Rate_ROW_Import_NonResale_Postponed_VAT_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VDEU&PA", "tax_xml": "ti_rtd_report.T44_Standard_Rate_23pct_ROW_Import_Resale_Postponed_VAT_RC_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VDEU&PA", "tax_xml": "ti_rtd_report.T45_Standard_Rate_23pct_ROW_Import_NonResale_Postponed_VAT_RC_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VDEU&PA", "tax_xml": "ti_rtd_report.T24_Reduced_rated_purchases_from_suppliers_EC_Services_13_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "+VDEU&PA", "tax_xml": "ti_rtd_report.T8_Standard_Rated_EC_Goods_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VDEU&PA", "tax_xml": "ti_rtd_report.T46_Zero_Rate_ROW_Import_Resale_Postponed_VAT_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VDEU&PA", "tax_xml": "ti_rtd_report.T47_Zero_Rate_ROW_Import_NonResale_Postponed_VAT_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VDEU&PA", "tax_xml": "ti_rtd_report.T48_Reduced_Rate_ROW_Import_Resale_Postponed_VAT_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VDEU&PA", "tax_xml": "ti_rtd_report.T49_Reduced_Rate_ROW_Import_NonResale_Postponed_VAT_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VDEU&PA", "tax_xml": "ti_rtd_report.T44_Standard_Rate_23pct_ROW_Import_Resale_Postponed_VAT_RC_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VDEU&PA", "tax_xml": "ti_rtd_report.T45_Standard_Rate_23pct_ROW_Import_NonResale_Postponed_VAT_RC_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VDEU&PA", "tax_xml": "ti_rtd_report.T24_Reduced_rated_purchases_from_suppliers_EC_Services_13_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
    {"tag": "-VDEU&PA", "tax_xml": "ti_rtd_report.T8_Standard_Rated_EC_Goods_23pct_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "tax", "factor_percent": 100},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T24_Reduced_rated_purchases_from_suppliers_EC_Services_13_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T38_Import_Services_Reverse_Charges", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T60_Import_Services_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T61_Import_Goods_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T46_Zero_Rate_ROW_Import_Resale_Postponed_VAT_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T47_Zero_Rate_ROW_Import_NonResale_Postponed_VAT_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T48_Reduced_Rate_ROW_Import_Resale_Postponed_VAT_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T49_Reduced_Rate_ROW_Import_NonResale_Postponed_VAT_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T8_Standard_Rated_EC_Goods_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T44_Standard_Rate_23pct_ROW_Import_Resale_Postponed_VAT_RC_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T45_Standard_Rate_23pct_ROW_Import_NonResale_Postponed_VAT_RC_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T4_135pct_Purchases_for_Resale_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T2_23pct_Standard_Rate_Purchase_for_Resale_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T18_Exempt_Transactions", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T0_Zero_Rated", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T7_135_purchases_not_for_resale", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T12_9_purchases_not_for_resale", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T6_23pct_Standard_Purchases_Not_For_Resale", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOPV", "tax_xml": "ti_rtd_report.T40_Import_of_Goods_Outside_EU_VAT_Paid_Point_of_Entry", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T24_Reduced_rated_purchases_from_suppliers_EC_Services_13_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T38_Import_Services_Reverse_Charges", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T60_Import_Services_23pct_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T61_Import_Goods_23pct_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T46_Zero_Rate_ROW_Import_Resale_Postponed_VAT_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T47_Zero_Rate_ROW_Import_NonResale_Postponed_VAT_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T48_Reduced_Rate_ROW_Import_Resale_Postponed_VAT_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T49_Reduced_Rate_ROW_Import_NonResale_Postponed_VAT_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T8_Standard_Rated_EC_Goods_23pct_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T44_Standard_Rate_23pct_ROW_Import_Resale_Postponed_VAT_RC_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T45_Standard_Rate_23pct_ROW_Import_NonResale_Postponed_VAT_RC_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T4_135pct_Purchases_for_Resale_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T2_23pct_Standard_Rate_Purchase_for_Resale_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T18_Exempt_Transactions", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T0_Zero_Rated", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T7_135_purchases_not_for_resale", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T12_9_purchases_not_for_resale", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T6_23pct_Standard_Purchases_Not_For_Resale", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOPV", "tax_xml": "ti_rtd_report.T40_Import_of_Goods_Outside_EU_VAT_Paid_Point_of_Entry", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOSV", "tax_xml": "ti_rtd_report.T18S_Exempt_Sales_Transactions", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOSV", "tax_xml": "ti_rtd_report.T42_Export_of_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOSV", "tax_xml": "ti_rtd_report.T43_Export_of_goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOSV", "tax_xml": "ti_rtd_report.T19_RCT_Sales", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOSV", "tax_xml": "ti_rtd_report.T21_Reverse_Charges_Reduced_Rate", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOSV", "tax_xml": "ti_rtd_report.T3_135_Sales", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "+NOSV", "tax_xml": "ti_rtd_report.T1_23pct_Standard_Rate_Sales", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOSV", "tax_xml": "ti_rtd_report.T18S_Exempt_Sales_Transactions", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOSV", "tax_xml": "ti_rtd_report.T42_Export_of_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOSV", "tax_xml": "ti_rtd_report.T43_Export_of_goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOSV", "tax_xml": "ti_rtd_report.T19_RCT_Sales", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOSV", "tax_xml": "ti_rtd_report.T21_Reverse_Charges_Reduced_Rate", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOSV", "tax_xml": "ti_rtd_report.T3_135_Sales", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},
{
    "tag": "-NOSV", "tax_xml": "ti_rtd_report.T1_23pct_Standard_Rate_Sales", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
},

    {
        "tag": "+baseT18S", "tax_xml": "ti_rtd_report.T18S_Exempt_Sales_Transactions", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT18S", "tax_xml": "ti_rtd_report.T18S_Exempt_Sales_Transactions", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT42", "tax_xml": "ti_rtd_report.T42_Export_of_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT42", "tax_xml": "ti_rtd_report.T42_Export_of_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT43", "tax_xml": "ti_rtd_report.T43_Export_of_goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT43", "tax_xml": "ti_rtd_report.T43_Export_of_goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT19", "tax_xml": "ti_rtd_report.T19_RCT_Sales", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT19", "tax_xml": "ti_rtd_report.T19_RCT_Sales", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT21", "tax_xml": "ti_rtd_report.T21_Reverse_Charges_Reduced_Rate", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT21", "tax_xml": "ti_rtd_report.T21_Reverse_Charges_Reduced_Rate", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT3", "tax_xml": "ti_rtd_report.T3_135_Sales", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT3", "tax_xml": "ti_rtd_report.T3_135_Sales", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT24", "tax_xml": "ti_rtd_report.T24_Reduced_rated_purchases_from_suppliers_EC_Services_13_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT24", "tax_xml": "ti_rtd_report.T24_Reduced_rated_purchases_from_suppliers_EC_Services_13_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT38", "tax_xml": "ti_rtd_report.T38_Import_Services_Reverse_Charges", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT38", "tax_xml": "ti_rtd_report.T38_Import_Services_Reverse_Charges", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT1", "tax_xml": "ti_rtd_report.T1_23pct_Standard_Rate_Sales", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT1", "tax_xml": "ti_rtd_report.T1_23pct_Standard_Rate_Sales", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT60", "tax_xml": "ti_rtd_report.T60_Import_Services_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT60", "tax_xml": "ti_rtd_report.T60_Import_Services_23pct_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT61", "tax_xml": "ti_rtd_report.T61_Import_Goods_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT61", "tax_xml": "ti_rtd_report.T61_Import_Goods_23pct_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT46", "tax_xml": "ti_rtd_report.T46_Zero_Rate_ROW_Import_Resale_Postponed_VAT_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT46", "tax_xml": "ti_rtd_report.T46_Zero_Rate_ROW_Import_Resale_Postponed_VAT_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT47", "tax_xml": "ti_rtd_report.T47_Zero_Rate_ROW_Import_NonResale_Postponed_VAT_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT47", "tax_xml": "ti_rtd_report.T47_Zero_Rate_ROW_Import_NonResale_Postponed_VAT_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT48", "tax_xml": "ti_rtd_report.T48_Reduced_Rate_ROW_Import_Resale_Postponed_VAT_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT48", "tax_xml": "ti_rtd_report.T48_Reduced_Rate_ROW_Import_Resale_Postponed_VAT_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT49", "tax_xml": "ti_rtd_report.T49_Reduced_Rate_ROW_Import_NonResale_Postponed_VAT_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT49", "tax_xml": "ti_rtd_report.T49_Reduced_Rate_ROW_Import_NonResale_Postponed_VAT_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT8", "tax_xml": "ti_rtd_report.T8_Standard_Rated_EC_Goods_23pct_RC", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT8", "tax_xml": "ti_rtd_report.T8_Standard_Rated_EC_Goods_23pct_RC", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT44", "tax_xml": "ti_rtd_report.T44_Standard_Rate_23pct_ROW_Import_Resale_Postponed_VAT_RC_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT44", "tax_xml": "ti_rtd_report.T44_Standard_Rate_23pct_ROW_Import_Resale_Postponed_VAT_RC_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT45", "tax_xml": "ti_rtd_report.T45_Standard_Rate_23pct_ROW_Import_NonResale_Postponed_VAT_RC_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT45", "tax_xml": "ti_rtd_report.T45_Standard_Rate_23pct_ROW_Import_NonResale_Postponed_VAT_RC_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT4", "tax_xml": "ti_rtd_report.T4_135pct_Purchases_for_Resale_Services", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT4", "tax_xml": "ti_rtd_report.T4_135pct_Purchases_for_Resale_Services", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT2", "tax_xml": "ti_rtd_report.T2_23pct_Standard_Rate_Purchase_for_Resale_Goods", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT2", "tax_xml": "ti_rtd_report.T2_23pct_Standard_Rate_Purchase_for_Resale_Goods", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT18", "tax_xml": "ti_rtd_report.T18_Exempt_Transactions", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT18", "tax_xml": "ti_rtd_report.T18_Exempt_Transactions", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT0", "tax_xml": "ti_rtd_report.T0_Zero_Rated", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT0", "tax_xml": "ti_rtd_report.T0_Zero_Rated", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT7", "tax_xml": "ti_rtd_report.T7_135_purchases_not_for_resale", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT7", "tax_xml": "ti_rtd_report.T7_135_purchases_not_for_resale", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT12", "tax_xml": "ti_rtd_report.T12_9_purchases_not_for_resale", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT12", "tax_xml": "ti_rtd_report.T12_9_purchases_not_for_resale", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT6", "tax_xml": "ti_rtd_report.T6_23pct_Standard_Purchases_Not_For_Resale", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT6", "tax_xml": "ti_rtd_report.T6_23pct_Standard_Purchases_Not_For_Resale", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "+baseT40", "tax_xml": "ti_rtd_report.T40_Import_of_Goods_Outside_EU_VAT_Paid_Point_of_Entry", "line_field": "invoice_repartition_line_ids", "repartition_type": "base"
    },
    {
        "tag": "-baseT40", "tax_xml": "ti_rtd_report.T40_Import_of_Goods_Outside_EU_VAT_Paid_Point_of_Entry", "line_field": "refund_repartition_line_ids", "repartition_type": "base"
    }



]



    for entry in special_tag_mappings_all:
        try:
            tax = env.ref(entry['tax_xml'])
        except ValueError:
            continue  # tax not found, skip this entry

        tag = Tag.search([("name", "=", entry["tag"])], limit=1)

        if tag:
            if entry["line_field"] == "invoice_repartition_line_ids":
                for line in tax.invoice_repartition_line_ids:
                    if line.repartition_type == entry["repartition_type"]:
                        # Apply factor_percent if it exists
                        if 'factor_percent' in entry:
                            if  entry["factor_percent"] == line.factor_percent:
                                line.write({"tag_ids": [(4, tag.id)]})
                        else:
                            # If no factor_percent, just apply the tag normally
                            line.write({"tag_ids": [(4, tag.id)]})

            elif entry["line_field"] == "refund_repartition_line_ids":
                for line in tax.refund_repartition_line_ids:
                    if line.repartition_type == entry["repartition_type"]:
                        # Apply factor_percent if it exists
                        if 'factor_percent' in entry:
                            # Check if the factor_percent matches
                            if  entry["factor_percent"] == line.factor_percent:
                                line.write({"tag_ids": [(4, tag.id)]})
                        else:
                            # If no factor_percent, just apply the tag normally
                            line.write({"tag_ids": [(4, tag.id)]})



def uninstall_hook(env):
    xml_ids_to_remove = [
        'ti_rtd_report.T18S_Exempt_Sales_Transactions',
        'ti_rtd_report.T42_Export_of_Services',
        'ti_rtd_report.T43_Export_of_goods',
        'ti_rtd_report.T19_RCT_Sales',
        'ti_rtd_report.T21_Reverse_Charges_Reduced_Rate',
        'ti_rtd_report.T3_135_Sales',
        'ti_rtd_report.T24_Reduced_rated_purchases_from_suppliers_EC_Services_13_RC',
        'ti_rtd_report.T38_Import_Services_Reverse_Charges',
        'ti_rtd_report.T1_23pct_Standard_Rate_Sales',
        'ti_rtd_report.T60_Import_Services_23pct_RC',
        'ti_rtd_report.T61_Import_Goods_23pct_RC',
        'ti_rtd_report.T46_Zero_Rate_ROW_Import_Resale_Postponed_VAT_Goods',
        'ti_rtd_report.T47_Zero_Rate_ROW_Import_NonResale_Postponed_VAT_Goods',
        'ti_rtd_report.T48_Reduced_Rate_ROW_Import_Resale_Postponed_VAT_Services',
        'ti_rtd_report.T49_Reduced_Rate_ROW_Import_NonResale_Postponed_VAT_Services',
        'ti_rtd_report.T8_Standard_Rated_EC_Goods_23pct_RC',
        'ti_rtd_report.T44_Standard_Rate_23pct_ROW_Import_Resale_Postponed_VAT_RC_Goods',
        'ti_rtd_report.T45_Standard_Rate_23pct_ROW_Import_NonResale_Postponed_VAT_RC_Goods',
        'ti_rtd_report.T4_135pct_Purchases_for_Resale_Services',
        'ti_rtd_report.T2_23pct_Standard_Rate_Purchase_for_Resale_Goods',
        'ti_rtd_report.T18_Exempt_Transactions',
        'ti_rtd_report.T0_Zero_Rated',
        'ti_rtd_report.T7_135_purchases_not_for_resale',
        'ti_rtd_report.T12_9_purchases_not_for_resale',
        'ti_rtd_report.T6_23pct_Standard_Purchases_Not_For_Resale',
        'ti_rtd_report.T40_Import_of_Goods_Outside_EU_VAT_Paid_Point_of_Entry',
        'ti_rtd_report.rtd_report',
        'ti_rtd_report.vat_return',
    ]

    for xml_id in xml_ids_to_remove:
        record = env.ref(xml_id, raise_if_not_found=False)
        if record:
            record_name = f"({record.display_name})"
            try:
                record.unlink()
            except Exception as e:
                raise ValidationError(
                    f"This app cannot be uninstalled because the record is still in use:\n\n{record_name}\n\n{str(e)}"
                )
