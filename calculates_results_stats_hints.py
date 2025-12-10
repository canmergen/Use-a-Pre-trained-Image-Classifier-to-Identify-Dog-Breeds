Aşağıda paylaştığın tabloyu doğru mantık sırasıyla, TMD’ye uygun, net ve kapsamlı şekilde açıklayan profesyonel bir metin bulunuyor.

Bu metin, senin söylediğin üç ana mantığı birebir takip ediyor:
	1.	332 doküman → 323 okunabilir → 218 tam okundu → 105 hata
	2.	PDF/TIFF kırılımındaki okuma performansı
	3.	Tüm dataset / Ground Truth / Readable Ground Truth için genel okuma oranları

⸻

Final OCR Performance and Readability Analysis (TMD Section)

This section explains the final and most operationally critical stage of the Hazirun Cetveli pipeline: the OCR readability and table extraction performance. While the model effectively identifies true Hazirun documents, the ultimate success of the system depends on whether these documents can be fully read and transformed into structured tables.

⸻

1. Post-Model Document Set: Hazirun or Non-Hazirun Selection

After the model filters the overall population, a total of 332 documents remain in scope for table extraction. These represent all documents that the model has identified as potentially relevant for Hazirun table reconstruction.

The OCR readability results for these 332 documents are as follows:

Metric	Count	Ratio
Total Model-Selected Docs	332	100%
Readable Docs (OCR can detect table content)	323	97.29%
Fully Readable Docs (OCR extracted entire table correctly)	218	67.49%
Failed OCR (partially unreadable or structurally broken)	105	32.51%

Interpretation
	•	Out of 332 incoming documents, almost all (323) are technically readable by OCR.
	•	However, only 218 documents contain table structures that can be extracted completely and without error.
	•	The remaining 105 documents contain issues such as broken lines, skewed pages, incomplete table capture, or low-quality scans.

Thus, OCR quality becomes the main limiting factor in table reconstruction—not the model classification.

⸻

2. PDF vs TIFF Readability Performance

Because document quality varies significantly by format, readability must also be evaluated separately for PDF and TIFF documents.

PDF Documents

Metric	Count	Ratio
Model-Selected PDF Docs	226	
Readable PDFs	220	
Fully Readable PDFs	158	71.82%
OCR Failures	62	28.18%

TIFF Documents

Metric	Count	Ratio
Model-Selected TIFF Docs	106	
Readable TIFFs	103	
Fully Readable TIFFs	60	58.25%
OCR Failures	43	41.75%

Interpretation
	•	PDF documents achieve a higher full-read success rate (71.82%) because their scanning quality is generally better.
	•	TIFF documents suffer more degradation, reflected in a lower 58.25% full-read rate and high OCR failure ratio.
	•	These differences are expected and consistent with earlier observations regarding TIFF quality issues.

⸻

3. Overall Dataset OCR Performance (Full Population Perspective)

Your table also summarizes how the OCR behaves not only on the model-selected subset, but across the entire dataset and across the ground truth population.

3.1. All 547 Documents

Regardless of model prediction, pure OCR performance across the entire input population is:

Category	Total	Successfully Read	Read Ratio
All Docs	547	218	39.85%

Interpretation

OCR alone can correctly extract only 40% of all documents, mostly due to low scan quality, missing tables, or structural anomalies.

⸻

3.2. Ground Truth Hazirun Documents (355 True Hazirun)

Category	Total	Successfully Read	Read Ratio
Ground Truth Hazirun	355	218	61.41%

Interpretation

Among the real Hazirun population:
	•	More than half (61.41%) can be successfully read.
	•	This reflects the inherent limitations of the document archive quality, not the model.

⸻

3.3. Readable Ground Truth Hazirun (323 Readable Docs)

Finally, when focusing only on documents that OCR marks as readable (323 documents):

Category	Total (Readable Docs)	Fully Read	Ratio
Readable Hazirun	323	218	67.49%

Interpretation

This metric represents the true operational efficiency of the pipeline.
Among the documents that can technically be read by OCR:

→ 2 out of every 3 Hazirun documents can be fully extracted into table format.

This is the core success metric for the Hazirun Table Extraction Model.

⸻

4. Final Operational Interpretation

Putting all results together:
	1.	Model Classification Phase
Successfully reduces noise and isolates the correct Hazirun documents.
	2.	OCR Readability Phase
Out of 332 model-selected documents, OCR can process 323.
	3.	Table Reconstruction Phase (Final Stage)
Only 218 documents produce full and accurate Hazirun tables.
	4.	Key Insight
The primary limiting factor in the end-to-end success rate is not the model’s classification accuracy, but the document scan quality and OCR compatibility.
	5.	Overall Achievement
The pipeline produces a clean, accurate, and reconstructible Hazirun dataset, extracted automatically from imperfect archival documents.

⸻

Hazırsan bu bölümün İngilizcesini de aynı şekilde hazırlayabilirim.