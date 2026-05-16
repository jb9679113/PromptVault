import { useState, useCallback } from 'react';
import { Sidebar } from './components/Sidebar';
import { PromptCard, EmptyState, StatsBar } from './components/PromptCard';
import { PromptModal, DeleteConfirmModal, SearchInput, AddButton } from './components/Modal';
import { usePromptManager } from './hooks/usePromptManager';
import { PromptItem } from './types';

function App() {
  const {
    filteredPrompts,
    isLoading,
    filter,
    tags,
    addPrompt,
    updatePrompt,
    deletePrompt,
    toggleFavorite,
    exportData,
    importData,
    updateFilter,
    totalCount,
  } = usePromptManager();

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingPrompt, setEditingPrompt] = useState<PromptItem | null>(null);
  const [deleteConfirm, setDeleteConfirm] = useState<{ id: string; title: string } | null>(null);
  const [showMobileSidebar, setShowMobileSidebar] = useState(false);

  // Handle add/edit prompt
  const handleSavePrompt = useCallback((prompt: Omit<PromptItem, 'id' | 'createdAt' | 'updatedAt'>) => {
    if (editingPrompt) {
      updatePrompt(editingPrompt.id, prompt);
    } else {
      addPrompt(prompt);
    }
    setEditingPrompt(null);
  }, [addPrompt, updatePrompt, editingPrompt]);

  // Handle edit click
  const handleEdit = useCallback((prompt: PromptItem) => {
    setEditingPrompt(prompt);
    setIsModalOpen(true);
    setShowMobileSidebar(false);
  }, []);

  // Handle delete click
  const handleDelete = useCallback((id: string) => {
    const prompt = filteredPrompts().find(p => p.id === id);
    if (prompt) {
      setDeleteConfirm({ id, title: prompt.title });
    }
  }, [filteredPrompts]);

  // Confirm delete
  const confirmDelete = useCallback(() => {
    if (deleteConfirm) {
      deletePrompt(deleteConfirm.id);
      setDeleteConfirm(null);
    }
  }, [deleteConfirm, deletePrompt]);

  // Handle import
  const handleImport = useCallback(async (file: File) => {
    const success = await importData(file);
    if (!success) {
      alert('导入失败，请确保文件格式正确');
    }
  }, [importData]);

  // Get popular tags (tags with most prompts)
  const popularTags = [...tags]
    .sort((a, b) => b.count - a.count)
    .map(t => t.name);

  const prompts = filteredPrompts();

  return (
    <div className="min-h-screen bg-slate-950">
      {/* Mobile sidebar overlay */}
      {showMobileSidebar && (
        <div
          className="fixed inset-0 bg-black/50 z-50 lg:hidden"
          onClick={() => setShowMobileSidebar(false)}
        />
      )}

      {/* Sidebar */}
      <Sidebar
        tags={tags}
        filter={filter}
        onFilterChange={(updates) => {
          updateFilter(updates);
          setShowMobileSidebar(false);
        }}
        onExport={exportData}
        onImport={handleImport}
        totalCount={totalCount}
        className={`lg:translate-x-0 transition-transform z-50 ${
          showMobileSidebar ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'
        }`}
      />

      {/* Main Content */}
      <main className="lg:ml-64 min-h-screen">
        {/* Mobile header */}
        <div className="lg:hidden bg-slate-900 border-b border-slate-700 px-4 py-3">
          <button
            onClick={() => setShowMobileSidebar(true)}
            className="text-slate-300 hover:text-white mr-4"
          >
            <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
          <span className="text-white font-bold">PromptVault</span>
        </div>

        {/* Top Toolbar */}
        <div className="sticky top-0 z-30 bg-slate-900/95 backdrop-blur-sm border-b border-slate-700 px-6 py-4">
          <div className="flex items-center justify-between gap-4 flex-wrap">
            <SearchInput
              value={filter.searchTerm}
              onChange={(value) => updateFilter({ searchTerm: value })}
            />
            <AddButton onClick={() => {
              setEditingPrompt(null);
              setIsModalOpen(true);
            }} />
          </div>

          {/* Stats Bar */}
          <StatsBar totalCount={totalCount} popularTags={popularTags} />
        </div>

        {/* Content Area */}
        <div className="p-6">
          {isLoading ? (
            <div className="flex items-center justify-center py-20">
              <div className="w-8 h-8 border-4 border-violet-500 border-t-transparent rounded-full animate-spin" />
            </div>
          ) : prompts.length > 0 ? (
            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
              {prompts.map(prompt => (
                <PromptCard
                  key={prompt.id}
                  prompt={prompt}
                  onToggleFavorite={toggleFavorite}
                  onEdit={handleEdit}
                  onDelete={handleDelete}
                />
              ))}
            </div>
          ) : (
            <EmptyState
              onAddClick={() => {
                setEditingPrompt(null);
                setIsModalOpen(true);
              }}
              searchTerm={filter.searchTerm}
            />
          )}
        </div>
      </main>

      {/* Modals */}
      <PromptModal
        isOpen={isModalOpen}
        onClose={() => {
          setIsModalOpen(false);
          setEditingPrompt(null);
        }}
        onSave={handleSavePrompt}
        editPrompt={editingPrompt}
      />

      <DeleteConfirmModal
        isOpen={!!deleteConfirm}
        onClose={() => setDeleteConfirm(null)}
        onConfirm={confirmDelete}
        title={deleteConfirm?.title || ''}
      />
    </div>
  );
}

export default App;
