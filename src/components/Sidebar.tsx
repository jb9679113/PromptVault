import { useState, useRef } from 'react';
import { Box, Star, Upload, Download, ChevronLeft, ChevronRight, LayoutDashboard } from 'lucide-react';

interface SidebarProps {
  tags: { name: string; count: number }[];
  filter: {
    selectedTag: string | null;
    showFavoritesOnly: boolean;
  };
  onFilterChange: (updates: { selectedTag?: string | null; showFavoritesOnly?: boolean }) => void;
  onExport: () => void;
  onImport: (file: File) => void;
  totalCount: number;
  className?: string;
}

export function Sidebar({
  tags,
  filter,
  onFilterChange,
  onExport,
  onImport,
  totalCount,
  className = '',
}: SidebarProps) {
  const [isCollapsed, setIsCollapsed] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleImportClick = () => {
    fileInputRef.current?.click();
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      onImport(file);
    }
    e.target.value = '';
  };

  return (
    <aside
      className={`fixed left-0 top-0 h-screen bg-slate-900 border-r border-slate-700 transition-all duration-300 z-40 ${className} ${
        isCollapsed ? 'w-16' : 'w-64'
      }`}
    >
      {/* Toggle Button */}
      <button
        onClick={() => setIsCollapsed(!isCollapsed)}
        className="absolute -right-3 top-6 w-6 h-6 bg-slate-700 hover:bg-slate-600 rounded-full flex items-center justify-center text-slate-300 hover:text-white transition-colors"
      >
        {isCollapsed ? <ChevronRight className="w-4 h-4" /> : <ChevronLeft className="w-4 h-4" />}
      </button>

      <div className="flex flex-col h-full py-6 px-3">
        {/* Brand */}
        <div className="flex items-center gap-3 mb-8 px-2">
          <div className="w-10 h-10 bg-gradient-to-br from-violet-500 to-indigo-600 rounded-xl flex items-center justify-center">
            <Box className="w-5 h-5 text-white" />
          </div>
          {!isCollapsed && (
            <div className="overflow-hidden">
              <h1 className="text-lg font-bold text-white truncate">PromptVault</h1>
              <p className="text-xs text-slate-400 truncate">AI Prompt Manager</p>
            </div>
          )}
        </div>

        {/* Quick Filters */}
        <div className="mb-6">
          {!isCollapsed && <h3 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3 px-2">快速过滤器</h3>}
          <div className="space-y-1">
            <button
              onClick={() => onFilterChange({ selectedTag: null, showFavoritesOnly: false })}
              className={`w-full flex items-center gap-2 px-3 py-2.5 rounded-lg transition-all ${
                !filter.selectedTag && !filter.showFavoritesOnly
                  ? 'bg-violet-600 text-white'
                  : 'text-slate-300 hover:bg-slate-800 hover:text-white'
              }`}
            >
              <LayoutDashboard className="w-4 h-4 flex-shrink-0" />
              {!isCollapsed && (
                <span className="truncate">全部提示词</span>
              )}
              {!isCollapsed && (
                <span className={`ml-auto text-xs px-2 py-0.5 rounded-full ${
                  !filter.selectedTag && !filter.showFavoritesOnly
                    ? 'bg-white/20'
                    : 'bg-slate-700'
                }`}>
                  {totalCount}
                </span>
              )}
            </button>

            <button
              onClick={() => onFilterChange({ selectedTag: null, showFavoritesOnly: !filter.showFavoritesOnly })}
              className={`w-full flex items-center gap-2 px-3 py-2.5 rounded-lg transition-all ${
                filter.showFavoritesOnly
                  ? 'bg-violet-600 text-white'
                  : 'text-slate-300 hover:bg-slate-800 hover:text-white'
              }`}
            >
              <Star className={`w-4 h-4 flex-shrink-0 ${filter.showFavoritesOnly ? 'fill-current' : ''}`} />
              {!isCollapsed && (
                <span className="truncate">我的收藏</span>
              )}
            </button>
          </div>
        </div>

        {/* Tags Section */}
        <div className="flex-1 overflow-hidden flex flex-col">
          {!isCollapsed && <h3 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3 px-2">标签</h3>}
          <div className="flex-1 overflow-y-auto space-y-1 pr-1">
            {tags.length > 0 ? (
              tags.map(tag => (
                <button
                  key={tag.name}
                  onClick={() => onFilterChange({
                    selectedTag: filter.selectedTag === tag.name ? null : tag.name,
                    showFavoritesOnly: false,
                  })}
                  className={`w-full flex items-center gap-2 px-3 py-2 rounded-lg transition-all ${
                    filter.selectedTag === tag.name
                      ? 'bg-violet-600 text-white'
                      : 'text-slate-300 hover:bg-slate-800 hover:text-white'
                  }`}
                >
                  <div className={`w-2 h-2 rounded-full ${
                    filter.selectedTag === tag.name ? 'bg-white/60' : 'bg-slate-500'
                  }`} />
                  {!isCollapsed && (
                    <>
                      <span className="truncate flex-1">{tag.name}</span>
                      <span className={`text-xs px-2 py-0.5 rounded-full ${
                        filter.selectedTag === tag.name
                          ? 'bg-white/20'
                          : 'bg-slate-700'
                      }`}>
                        {tag.count}
                      </span>
                    </>
                  )}
                </button>
              ))
            ) : (
              !isCollapsed && (
                <p className="text-slate-500 text-sm px-2">暂无标签</p>
              )
            )}
          </div>
        </div>

        {/* Bottom Actions */}
        <div className="mt-6 space-y-2">
          <button
            onClick={handleImportClick}
            className="w-full flex items-center gap-2 px-3 py-2.5 text-slate-300 hover:text-white hover:bg-slate-800 rounded-lg transition-all"
          >
            <Upload className="w-4 h-4 flex-shrink-0" />
            {!isCollapsed && <span>导入 JSON</span>}
          </button>
          <button
            onClick={onExport}
            className="w-full flex items-center gap-2 px-3 py-2.5 text-slate-300 hover:text-white hover:bg-slate-800 rounded-lg transition-all"
          >
            <Download className="w-4 h-4 flex-shrink-0" />
            {!isCollapsed && <span>导出 JSON</span>}
          </button>
        </div>

        {/* Hidden file input for import */}
        <input
          ref={fileInputRef}
          type="file"
          accept=".json"
          onChange={handleFileChange}
          className="hidden"
        />
      </div>
    </aside>
  );
}
